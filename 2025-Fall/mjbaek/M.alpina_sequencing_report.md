# 🧬 Mortierella alpina Genome Sequencing & Assembly Report

---

## 1️⃣ Background

### 🔬 Sequencing Platform
- **Sequencing platform**: Oxford Nanopore Technologies (ONT)
- **Flow cell**: FLO-MIN114 (R10.4.1)
- **Flow cell ID**: FBE72537
- **Library kit**: Ligation Sequencing Kit DNA V14 (SQK-LSK114)

### 🧠 Target Genome Characteristics
- **Estimated genome size**: ~38–40 Mb
- **GC content**: ~50–52%
- **Genomic features**:
  - 높은 유전자 중복도
  - 50개 이상으로 구성된 multigene family 다수 존재

> 위와 같은 특성으로 인해 short-read 기반 조립 시 misassembly 가능성이 높아,  
> long-read 기반 genome assembly 전략이 필수적이다.

---

## 2️⃣ Sample Preparation & Library Input Estimation

### 🧪 DNA Quality Check (gDNA 추출 후)
- **Gel electrophoresis**: High-molecular-weight DNA 확인
- **NanoDrop (A260/280)**: 1.864
- **Qubit concentration**: 38.8 ng/µL

### 📦 Library Loading 정보
- **Library concentration**: 20.4 ng/µL
- **Loading volume**: 12 µL
- **Assumed mean fragment length**: ~39 kb

#### 🧮 Molarity Estimation
- ~0.78 pmol/µL
- **Total loaded amount**: ~9.36 fmol

✅ ONT protocol에서 권장하는 loading 범위 (5–10 fmol)에 포함됨

---

## 3️⃣ Sequencing Output & Run Summary

### 📊 Data Yield
- **Total bases**: ~15.49 Gb
- **Total reads**: ~6.25 million
- **Estimated read N50**: ~5.49 kb

➡️ 예상 genome size (~40 Mb) 기준 약 **350× coverage** 확보

### ⏱ Run Duration
- **Configured runtime**: 72 h
- **Actual runtime**: ~57.5 h
- **Pore activity**:
  - 초기 약 80%
  - 종료 시 약 10%

> Active pore 비율이 10%대로 감소한 시점에서 sequencing을 종료했으며,  
> 이론적으로 assembly에 충분한 데이터가 확보된 상태였다.

---

## 4️⃣ Basecalling

### 🛠 Tool & Model
- **Basecaller**: Dorado v5.2.0
- **Model**: r1041_e82_400bps_sup

| 파라미터 | 의미 |
|--------|------|
| r1041 | R10.4.1 flow cell |
| e82 | Kit V14 pore chemistry |
| 400bps | Sequencing speed |
| sup | Super high accuracy model |

### 🧠 원리
> Dorado는 Nanopore의 raw electrical signal을  
> 딥러닝 모델을 이용해 염기서열로 변환하는 basecaller로,  
> `sup` 모델은 높은 정확도를 우선시한 설정이다.

---

## 5️⃣ Quality Control (Pre-filtering)

### 🛠 사용 툴
- **Falco**
- **NanoPlot**

### 🧠 툴 원리
- **Falco**: read 품질, 길이 분포, Q-score를 요약 분석
- **NanoPlot**: read 길이와 품질의 상관관계를 시각적으로 확인

### 📊 Raw Read QC 결과
- **Total bases**: ~16.8 Gb
- **Estimated coverage**: >400×
- **Mean Q-score**: 15.4
- **Mean read length**: ~2.56 kb
- **Read N50**: ~5.75 kb
- Q < 4 수준의 매우 낮은 품질 read 다수 존재

---

## 6️⃣ Read Filtering Strategy (Filtlong)

### 🧠 필터링 기준 설정 배경

#### 📌 품질 기준 (Falco 기반)
- 평균 Q-score 12 미만 read가 다수 존재
- 낮은 품질 read는 assembly 오류 및 노이즈 증가 가능
- `min_mean_q = 12` 기준 설정

#### 📌 길이 기준 (NanoPlot 기반)
- 5 kb 미만의 짧은 read에서 품질 저하 경향 확인
- assembly 기여도가 높은 read만 유지
- `min_length = 5000` bp 설정

#### 📌 품질 중심 전략
- 충분한 coverage가 확보되었으므로,
- 전체 read 중 **assembly 기여도가 높은 상위 read만 선별**

---

## 7️⃣ Read Filtering (Filtlong)

### 🛠 Tool
- **Filtlong**

### ⚙️ Parameters
- `min_length = 5000`
- `min_mean_q = 12`
- `keep_percent = 25`
- `mean_q_weight = 20`

🧠 Filtlong은 read의 길이와 품질을 종합적으로 평가하여  
assembly에 가장 유리한 read를 우선적으로 유지한다.

### 📁 Output
- `filtered.fastq`

---

## 8️⃣ Post-filtering Quality Control

### 🛠 Tool
- **NanoPlot**

### 📊 Filtering 이후 결과
- **Total reads**: 273,145
- **Total bases**: 4.20 Gb
- **Mean read length**: 15,378 bp
- **Median read length**: 13,474 bp
- **Read N50**: 16,107 bp

➡️ Filtering 전 대비 N50 약 **3배 증가**

### 📈 Quality Metrics
- **Mean Q-score**: 23.7
- **Median Q-score**: 24.0
- Q20 이상 read: 98.5%
- **Longest read**: 208 kb (Q ≈ 19)

---

## 9️⃣ Genome Assembly

### 🛠 Tool
- **Flye**

### ⚙️ Configuration
- **Mode**: `nano-hq`
- **Minimum overlap length**: 5000 bp

🧠 Flye는 long-read 기반 overlap graph를 구성하여  
반복서열을 고려한 genome assembly를 수행한다.

### 📁 Output
- `assembly.fasta`

---

## 🔟 Polishing (Error Correction)

### 🛠 Tool
- **Medaka**

### 🧠 원리
> Medaka는 원본 Nanopore read를 assembly에 재정렬하여  
> 딥러닝 모델 기반으로 indel 및 substitution 오류를 보정한다.

### ⚙️ Configuration
- **Model**: r1041_e82_400bps_sup_v5.2.0

### 📁 Output
- `consensus.fasta`
- 최종 genome size: **~37.5 Mb**

---

## 1️⃣1️⃣ Completeness Assessment (BUSCO)

### 🛠 Tool
- **BUSCO + miniprot**

### ⚙️ Configuration
- **Lineage**: Eukaryota
- **Mode**: Genome

### 📊 BUSCO Results
- **Complete**: 99.2% (253/255)
- **Fragmented**: 0.4%
- **Missing**: 0.4%

➡️ Polishing 이후 유전자 구조가 안정적으로 복원되었음을 시사

---

## 1️⃣2️⃣ Assembly Statistics

- **Total assembly length**: **39.29 Mb**
- **Number of contigs**: **18**
- **N50**: **~3 Mb**

---

## ✅ Final Assessment

- Nanopore 단독 데이터로 **높은 연속성(contig 18개)** 확보
- BUSCO completeness **99.2%**로 매우 우수한 품질
- NCBI reference (GCA_977091265.1)와 비교 시:
  - genome size 유사
  - contig 수 감소 → **더 높은 연속성 확보**

🚀 본 assembly는 유전자 예측, 비교유전체 분석 등 후속 분석에 적합함
