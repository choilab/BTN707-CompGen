# Mortierella alpina genome sequencing and assembly report

## 1. Background

### Platform 
- **Sequencing platform**: Oxford Nanopore Technologies (ONT)
- **Flow cell**: FLO-MIN114 (R10.4.1)
- **Flow cell ID**: FBE72537
- **Library kit**: Ligation Sequencing Kit DNA V14 (SQK-LSK114)

### Target Genome Characteristics
- **Estimated genome size**: ~38–40 Mb
- **GC content**: ~50–52%
- **Genomic feature**: High gene duplication (multigene families >50%)

---

## 2. Sample Preparation & Library Input Estimation

### DNA Quality Check after gDN
- **DNA condition check with gel electrophoresis**
- **NanoDrop**: 1.864
- **Qubit concentration**: 38.8 ng/µL

### Library Loading
- Library concentration: 20.4 ng/µL
- Loading volume: 12 µL
- Assumed mean fragment length: 39 kb

**Molarity estimation**:
- ~0.78 pmol/µL
- Total loaded amount: ~9.36 fmol
> 해당 DNA의 양은 ONT protocol에서 추천하는 범위(5–10 fmol)에 속함.

---

## 3. Sequencing Output & Run Summary

### Data Yield
- **Total bases**: ~15.49 Gb
- **Total reads**: ~6.25 million
- **Estimated read N50**: 5.49 kb

### Run Duration
- Configured: 72 hours  
- Actual runtime: ~57.5 hours  
- Pore activity: ~80% initially, dropped to ~10% before termination
> 이론적으로 충분한 양의 데이터(>15 Gb, 350x)를 얻었고, active한 pore가 10% 대로 내려왔을 때 sequencing stop.

---

## 4. Basecalling

### Tool & Model
- **Basecaller**: Dorado
- **Version**: v5.2.0
- **Model**: r1041_e82_400bps_sup

**Model parameters**:
- r1041: R10.4.1 flow cell
- e82: Kit V14-compatible pore chemistry
- 400bps: sequencing speed
- sup: super high accuracy model

### Output
- FASTQ files containing basecalled reads

---

## 5. Quality Control (Pre-filtering)

### Tools
- **Falco**
- **NanoPlot**

### Output-Key Metrics (Raw Reads)
- **Total bases**: ~16.8 Gb
- **Estimated coverage**: >400× (based on ~40 Mb genome)
- **Mean Q-score**: 15.4
- **Read length statistics**:
  - Mean length: ~2.56 kb
  - N50: ~5.75 kb
  - Presence of very long but low-quality reads (Q < 4)

### QC 결과를 기반으로 한 Filtlong 필터링 전략
**Falco 결과 → 품질 기준 설정**
- Falco 분석 결과, 평균 Q-score가 12 미만인 read가 다수 존재함을 확인함.
- Q-score 12(≈93% 정확도) 미만의 read는 조립 과정에서 오류와 노이즈를 증가시킬 가능성이 높음.
- 이에 따라 Filtlong에서 `min_mean_q = 12`를 최소 품질 기준으로 설정함.

**NanoPlot 결과 → 길이 기준 설정**
- NanoPlot 분석에서 짧은 read(<5 kb)는 품질이 낮은 경향을 보였고, 긴 read일수록 품질이 안정적이었음.
- 조립에 실질적으로 기여하는 read만 남기기 위해 `min_length = 5000` bp로 설정함.

**품질 중심 필터링 전략**
- 길이보다 품질이 조립 정확도에 더 중요하다고 판단함.
- Filtlong에서 `mean_q_weight` 값을 높게 설정하여 고품질 read가 우선적으로 선택되도록 함.

---

## 6. Read Filtering (Filtlong)

### Tool
- Filtlong

### Input
- basecalling 이후의 fastq파일

### Parameters(QC 결과 반영)
- min_length 5000, min_mean_q 12
- keep percent: 25%
  - 충분한 coverage(>400×)를 확보했기 때문에, 전체 데이터 중 assembly 기여도가 가장 높은 상위 25% 리드만 유지
- mean_q_weight 20

### Output
- filtered.fastq

---

## 7. Post-filtering Quality Control (NanoPlot)

### Tool
- NanoPlot

### Input
- filtered.fastq

### Purpose
- Filtlong filtering 이후 데이터 품질 변화 확인

---

### NanoPlot Summary (After Filtering)

#### Data Yield
- **Total reads**: 273,145
- **Total bases**: 4.20 Gb

#### Read Length Statistics
- **Mean read length**: 15,378 bp
- **Median read length**: 13,474 bp
- **Read N50**: 16,107 bp

> Filtering 전 N50 (~5.49 kb) 대비 약 3배 증가

#### Quality Metrics
- **Mean Q-score**: 23.7
- **Median Q-score**: 24.0

##### Quality Distribution
- Reads ≥ Q10: 100%
- Reads ≥ Q15: 100%
- Reads ≥ Q20: 98.5%
- Reads ≥ Q25: 28.7%
- Reads ≥ Q30: 3.1%

- **Highest Q-score**: 34.6

#### Long-read Characteristics
- **Longest read**: 208,053 bp (Q ≈ 19)
- 상위 초장기 리드들이 Q-score 18–20 범위 유지

---

### Interpretation

- 필터링 이후 전체 데이터량은 감소했으나, assembly에 기여도가 높은 리드만 유지됨
- read N50 및 평균 길이 증가로 long-read assembly에 유리한 분포 형성
- 평균 Q-score ~24 수준으로 base-level error 감소 기대

---

## 8. Genome Assembly

### Tool
- Flye

### Input
- filtered.fastq

### Mode
- nano-hq (Nanopore high-quality reads)

### Key Parameter
- **Minimum overlap length: 5000 bp**
- Filtlong에서 최소 read length를 5 kb로 설정했으므로 assembly 단계에서도 동일한 기준을 적용
- 짧은 overlap으로 인한 잘못된 contig 연결 방지
- 고신뢰 overlap 기반 assembly graph 생성 목적

### Output
- assembly.fasta


## 9. Polishing (Error Correction)

### Tool
- **Medaka**

### Purpose
조립된 contig 서열 위에 원래의 고품질 Nanopore 리드들을 다시 정렬하여,
염기 삽입/결실(indel) 및 치환 오류를 인공지능 기반 모델로 보정함.
Assembly 단계에서 남을 수 있는 미세한 base-level 오류를 제거하는 과정이다.

### Configuration
- **Model**: r1041_e82_400bps_sup_v5.2.0
- **Input**: assembly.fasta (Flye 결과)
- **Output**: consensus.fasta

### Result
- 최종 consensus 서열 크기: **~37.5 MB**
- Mucor alpina의 예상 게놈 크기 범위 내에서 안정적으로 조립된 것으로 판단됨
- 후속 유전자 예측 및 completeness 평가에 적합한 품질 확보


---

## 10. Completeness Assessment

### Purpose
조립된 게놈이 생물학적으로 얼마나 완전한지 평가하기 위해,
진핵생물이 공통적으로 보유해야 하는 **필수 유전자 세트**의 존재 여부를 확인함.

### Tool
- **BUSCO (with miniprot gene predictor)**

### Configuration
- **Lineage**: Eukaryota
- **Mode**: Genome assembly
- **Gene predictor**: Auto-detect (eukaryotes)

---

### BUSCO Result Interpretation

#### 1. Quality (Gene Completeness)

- **Complete (C): 99.2%**
  - 전체 255개의 필수 유전자 중 **253개가 완전한 형태로 검출**
  - 조립된 게놈에 생물학적 결손이 거의 없음을 의미
  - 일반적으로 95% 이상이면 매우 우수한 품질로 평가됨

- **Fragmented (F): 0.4%**
  - 일부만 검출된 유전자 1개
  - 잔존하는 조립 또는 염기 수준 오류 가능성은 매우 낮음

- **Missing (M): 0.4%**
  - 미검출 유전자 1개
  - 데이터 부족 또는 해당 종 특이적 유전자 변이 가능성

→ Medaka polishing 이후 유전자 구조가 안정적으로 복원되었음을 시사함

---

#### 2. Assembly Structure (Continuity)

- **Total assembly length**: **39,288,763 bp (~39.3 Mb)**
  - M. alpina의 보고된 게놈 크기 (38–45 Mb) 범위에 정확히 부합
  - 과잉 조립(over-assembly) 또는 결손 없이 적절한 데이터량 사용

- **Number of contigs**: **18**
  - 약 40 Mb 규모의 게놈이 18개 contig로 구성됨
  - 높은 연속성(continuity)을 가진 assembly

- **N50**: **~3 Mb**
  - contig의 절반 이상이 3 Mb 이상의 길이를 가짐

---

## Final Assessment

본 Nanopore 기반 분석과 고품질 read 위주의 assembly로 **높은 연속성(N50 ~3 Mb)**과 **완전성(BUSCO C 99.2%)**을 만족하는 genome 서열을 확보했다.
NCBI에서 확인한 M.alpina(id: GCA_977091265.1)와 분석을 비교해보았을 때,
<img width="950" height="1208" alt="image" src="https://github.com/user-attachments/assets/4bf23429-3753-4aa8-867e-4c8695e9a332" />

전체 genome 크기가 유사하며, contig는 우리가 확보한 contig가 더 적기에, 연속성이 높은 dna를 확보했다고 할 수 있다.

  

