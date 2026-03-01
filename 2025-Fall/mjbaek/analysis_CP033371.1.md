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

### Figure 1. 각 ID에 해당하는 유전자의 presence, absence의 matix파일로 나타낸 힛맵


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

# 5️⃣ Accessory Genome 기반 기능 분석 (CP033371.1)

CP033371.1이 pangenome 분석에서 outlier로 분리된 원인을 확인하기 위해  
gene presence/absence matrix 기반으로 특이 유전자를 추출하고,  
해당 유전자들의 기능 정보를 eggNOG annotation 결과와 매칭하여 분석하였다.

---

## 📌 (1) 입력 데이터

- Roary output: `gene_presence_absence.csv`
- eggNOG annotation 결과 파일 (전체 유전자 대상)
- 분석 대상 샘플: CP033371.1

---

## 🧬 (2) 유전자 추출 과정

### ① Presence/Absence 기반 코드 추출

`gene_presence_absence.csv` 파일에서 Python 스크립트를 이용하여 다음 두 그룹을 정의하였다:

- 🧬 CP033371.1에만 존재하고, 다른 모든 샘플에는 없는 유전자 → 115개
- ❌ CP033371.1에만 없고, 다른 모든 샘플에는 존재하는 유전자 → 374개

즉, CP033371.1에만 있거나 없는 액세서리 중에 액세서리 유전자들을 확보했다.

---

### ② eggNOG 결과의 coog와 매칭

- 위에서 추출한 유전자를 eggNOG annotation 결과 파일과 매칭

---

## 📊 (3) COG category 기반 기능 분포 분석

각 유전자 그룹(115 / 374)에 대해  
COG category별 유전자 수를 집계하였다.

### 🔻 CP033371.1 결여 유전자 (n = 374)

상대적으로 높은 비율을 보인 COG category:

- E: 아미노산 운반 및 대사
- G: 탄수화물 운반 및 대사
- F: 뉴클레오타이드 운반 및 대사

---

### 🔺 CP033371.1 고유 유전자 (n = 115)

상대적으로 높은 비율을 보인 COG category:

- J: 번역, 리보솜 구조 및 생합성
- H: 조효소 운반 및 대사

---

<img width="1490" height="989" alt="image" src="https://github.com/user-attachments/assets/cdff17ea-85f7-472e-b979-70e80c136b8c" />

### Figure 2. CP033371.1 특이 유전자의 COG category 분포

- X축: COG category
- Y축: 유전자 수
- 그룹 비교:
  - Unique(present) genes (115)
  - Absent genes (374)

해당 figure는 presence/absence 기반으로 정의된 두 유전자 그룹 간 cog 기능군 조성 차이를 시각적으로 비교하기 위해 작성되었다.

---

# 6️⃣ 기능적 패턴 요약

- 대사 관련 기능군(E, G, F)에서는 결여 유전자 비율이 높게 나타남
- 번역(J) 및 조효소(H) 관련 기능군에서는 고유 유전자 비율이 상대적으로 높게 나타남
  
이는 CP033371.1이 다른 균주들과 accessory gene 기능 조성 측면에서 차이를 보인다는 것을 의미한다.

---

# 7️⃣ Discussion: CP033371.1의 기능적 특성과 Fresh milk 환경

CP033371.1은 fresh milk에서 분리된 균주이며,  
Accessory genome 분석에서 다른 균주들과 구별되는 기능 조성 차이를 보였다.

---

## 🧬 1. 번역 관련 기능 (Category J)

CP033371.1 고유 유전자군에서  
번역 및 리보솜 관련 기능(J category)이 상대적으로 높게 나타났다.

리보솜 관련 유전자는 일반적으로 core genome에 포함되는 보존적 영역이지만,  
accessory 영역에서 해당 기능이 관찰되었다는 점은  
번역 조절 또는 리보솜 보조 단백질 수준의 차이를 시사할 수 있다.

이는 milk 환경에서의 빠른 성장 또는  
단백질 합성 조절과 관련될 가능성이 있다.

---

## 🧪 2. 조효소 대사 기능 (Category H)

CP033371.1에서는 조효소 운반 및 대사(H category) 관련 유전자가 상대적으로 많았다.

Fresh milk는 비교적 안정된 영양 환경이며  
비타민 및 일부 조효소가 존재하는 환경이다.

따라서 해당 유전자 증가는  
외부 조효소 활용 능력 또는 대사 조절 능력과 연관될 가능성이 있다.

---

## 🔻 3. 대사 기능의 일부 축소 (Category E, G)

반대로, CP033371.1에서는  
아미노산(E) 및 탄수화물(G) 대사 관련 유전자의 결여가 다수 관찰되었다.

이는 다양한 기질을 활용하는 범용 대사 전략보다는  
영양 구성이 비교적 일정한 milk 환경에 적응된  
제한적 대사 전략을 가질 가능성을 시사한다.

---

# 🔎 종합적으로

Core genome에서는 큰 계통적 분화가 관찰되지 않았으나,  
Accessory genome 수준에서는 기능 조성 차이가 명확하였다.

Fresh milk 유래라는 metadata를 고려할 때,  
CP033371.1의 outlier 특성은  
계통적 분화라기보다는 **환경 특이적 기능 조정(functional tuning)**에  
가깝게 해석될 수 있다.

해당 가설은 추가적인 발현 분석 및 대사 실험을 통해 검증이 필요하다.

