# 🧬 CP033371.1 (dataset_31) 비교유전체 분석

---

## 1️⃣ 분석 배경

Accessory genome 기반 계통수에서  
**CP033371.1 (Prokka_on_dataset_31__gff)**가 비정상적으로 긴 branch를 형성하며 아웃라이어로 나타났다.


따라서 본 분석의 목적은 다음과 같다.

> CP033371.1의 유전자 구성 및 변이 패턴이  
> 액세서리 유전자 기준으로만 특이적인지, 혹은 시퀀스 파일자체의 문제가 아닌지 등을 평가한다.

---

# 2️⃣ Accessory Genome 기반 분석

## 📂 (1) 입력 데이터

- Roary gene presence/absence matrix  
- `accessory_presence_absence_renamed.tsv`

---

## 🔥 (2) Presence/Absence Heatmap 분석

### 입력
- 전체 유전자 presence/absence binary matrix

### 결과

<img width="1800" height="1490" alt="image" src="https://github.com/user-attachments/assets/7f6955f9-6a40-41b4-a5c4-f596ef2c4af1" />


### 📊 관찰 결과 (heatmap기반 수치화)

- CP033371.1에서 상대적으로 많은 유전자 부재 관찰
- 총 8,858개 유전자 부재
- 다른 모든 균주에는 존재하지만 CP033371.1에만 없는 유전자: 374개
- CP033371.1에만 존재하는 유전자: 115개

👉 Accessory 기반 계통수에서 긴 branch가 형성된 원인은  
**Accessory gene 구성에서 뚜렷한 차이 존재 때문일 가능성이 높다.**
따라서, 해당 가설을 확인하기 위해서, core gene은 다른 sequence들과 차이가 있는 지 보았다.

---

# 3️⃣ Core Genome 기반 분석

Accessory 기반 아웃라이어 현상이 실제 계통학적 분화를 의미하는지 검증하기 위해 core genome 분석 수행.

---

## 📌 (1) 입력 데이터

- Roary Core Gene Alignment FASTA
- 총 81개 core gene
- 전체 정렬 길이: 364,673 bp
- 모든 샘플 동일 길이
- N 없음 (clean alignment)

---

## 🧬 (2) SNP 분석 결과

- 전체 polymorphic site: 23,309개
- dataset_31 평균 SNP 차이: 약 3,409개
- 전체 길이 대비 변이율: 약 0.93%
- polymorphic site 대비 기여율: 약 14.63%

### 📖 해석

- 전체 서열 대비 1% 미만 차이 → 높은 보존성
- Core gene 기능 유지 범위 내 다양성
- Core phylogeny에서도 큰 이탈 없었음

---

# 4️⃣ 종합 해석

| 분석 기준 | CP033371.1 특징 |
|------------|----------------|
| 🔎 ANI | 정상 범위 |
| 🌳 Core gene phylogeny | 큰 이탈 없음 |
| 🧬 SNP divergence | 종내 다양성 수준 |
| 📦 Accessory gene | 많은 유전자 부재 및 일부 특이 유전자 존재 |
| 📈 Accessory tree | 긴 branch 형성 |

---

# 5️⃣ 결론

CP033371.1은:

- 🧬 Core genome 수준에서는 정상적인 종내 변이 범위
- 📦 Accessory genome 구성에서 상대적으로 큰 차이 존재

따라서 accessory 기반 계통수에서의 아웃라이어 현상은  
**gene gain/loss에 의해 발생한 gene content 기반 분화 현상**으로 판단된다.

---

# 6️⃣ 🎯 다음 분석 목표: eggNOG 기능 분류 기반 비교

Accessory genome 차이가 단순한 유전자 수 차이인지,  
아니면 특정 기능군의 선택적 소실/확장인지 규명하기 위해  
**eggNOG functional annotation 기반 비교 분석**을 수행할 예정이다.

## 🔬 목표

1. CP033371.1 특이 유전자(115개)의 기능군 분류
2. CP033371.1에서 결손된 374개 유전자의 기능군 분류
3. COG category별 enrichment 분석
4. 기능군별 비율 비교 시각화 (barplot 또는 heatmap)

---

## 📝 한 문장 요약

> CP033371.1은 core genome에서는 정상 범위에 속하지만, accessory genome 구성에서 기능적 차이를 보이며, 이를 eggNOG 기반 기능 분류 분석을 통해 정밀하게 규명할 예정이다.
