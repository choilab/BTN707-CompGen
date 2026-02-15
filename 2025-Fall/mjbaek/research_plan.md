# 연구계획서  
## Optimization of Hispidin Synthase(PKS) Expression in E. coli

---

## 1. 연구 배경 및 문제 인식

버섯 유래 bioluminescent pathway (npgA, hisps, h3h, luz)는 비교적 적은 효소 수로 자가발광을 구현할 수 있는 매력적인 시스템이다. 그러나 해당 경로를 E. coli에서 안정적이고 재현성 있게 구현하는 데에는 다음과 같은 문제가 존재한다.

- 가장 큰 효소인 **Hispidin synthase (HispS, PKS)**의 발현이 불안정함
- 발현은 되더라도 발광이 재현성 있게 나타나지 않음
- colony 단계에서 직접적인 기능 기반 스크리닝이 어려움
- 효소 발현 burden 및 misfolding 가능성 존재

현재 yeast promoter를 그대로 사용한 시스템에서 간헐적 발광은 관찰되지만, 발현 강도와 활성 사이의 상관관계가 명확하지 않으며 E. coli 최적 조건이 규명되지 않은 상태이다.

---

## 2. 연구 목표

본 연구의 궁극적 목표는 다음과 같다.

> **E. coli에서 버섯 bioluminescent pathway, 특히 Hispidin synthase가 안정적으로 발현·활성될 수 있는 최적 조건을 규명하고, 재현성 있는 발광 시스템을 구축한다.**

이를 위해 두 가지 큰 전략이 존재한다.
- 전략 1. Promoter Engineering 기반 발현 강도 최적화
- 전략 2. Directed Evolution 기반 효소 기능 및 적응성 개선

---

# 전략 1. Promoter Engineering 기반 발현 강도 최적화

## 전략 개념

이 전략의 핵심 개념은 다음과 같다.

> PKS와 같은 대형 효소는 "적절한 발현 강도 범위(optimal expression window)"가 존재할 가능성이 높다.

너무 낮으면 활성이 부족하고,  
너무 높으면 misfolding·aggregation·metabolic burden이 발생할 수 있다.

따라서, **yeast 시스템에서의 기준 발현량을 정량화**한 뒤, 이를 바탕으로 E. coli promoter 강도 스펙트럼을 체계적으로 탐색한다.

---

## Aim 1. Yeast promoter 시스템의 발현 한계 정량화

### 목적

현재 yeast promoter 기반 시스템이 E. coli에서 어느 정도의 실효 발현을 유도하는지 정량화하여, 이후 promoter 설계의 기준값(reference)을 확보한다.

### 실험 내용

- 동일 플라스미드로 E. coli transformation
- qRT-PCR을 통한 mRNA 정량 (npgA, hisps, h3h, luz)
- Western blot 또는 tag 기반 단백질 정량
- 발광 강도 측정

### 기대 결과

- mRNA–단백질–활성 간 상관관계 확보
- “현재 시스템의 실제 발현 강도 범위” 정의
- 이후 E. coli promoter 선택 시 목표 강도 구간 설정

---

## Aim 2. E. coli promoter 라이브러리 구축 및 최적 강도 탐색

### 설계 개요

앞서 Aim 1.의 결과(Yeast 기준 발현량)를 바탕으로 Low–Medium–High 강도의 E. coli promoter/RBS 조합 라이브러리를 구축한다.

가설:

> PKS가 안정적으로 발현·활성되는 특정 발현 강도 구간이 존재한다.

가설 검증을 위한 방법은 두가지가 있다.

### 방법 (A) Constitutive promoter 기반 단계적 탐색

yeast에서 확인된 발현량을 기반으로 e.coli에서 비슷한 양으로 발현할 수 있는 프로모터로 교체.
이후 튜닝을 해가며 최적의 조건을 찾아감.

ex.
- 약한 promoter + 약한 RBS
- 약한 promoter + 중간 RBS
- 중간 promoter + 약한 RBS
- 중간 promoter + 중간 RBS

---

### 방법 (B) T7 기반 발현 전략

우리 연구실에는 이미 T7 기반 발현 벡터 및 bio-part가 구축되어 있다.

이를 활용하면:

- primer 설계 단순화
- 기존 backbone 활용 가능
- IPTG gradient를 통한 발현수준 조절, 그리고 유도체를 처리하기 전에 발광을 테스트해 leaky expression이 일어나는 수준에서의 발현량으로도 테스트 가능.

조건:
- 무유도 (leaky expression)
- IPTG 0.01–0.1 mM gradient

이를 통해:
- 저발현부터 고발현까지 넓은 스펙트럼 확보
- PKS의 허용 발현 범위 정의

---

# 전략 2. Directed Evolution 기반 효소 기능 및 적응성 개선

## 전략 개념

Promoter 조절은 “발현 강도”를 조절하는 접근이다.

반면, Directed evolution은 다음 질문에 답하기 위한 전략이다:

> 효소 자체가 E. coli 환경에 최적화되어 있지 않다면?

대형 PKS(HispS)와 NpgA는 진균 유래 효소로,  
E. coli 세포 환경에서 다음과 같은 문제가 발생할 수 있다:

- folding inefficiency
- host factor 의존성
- cofactor 상호작용 차이
- metabolic incompatibility

따라서 효소 자체를 활성이 좋은 서열을 가지도록 진화시키는 전략을 도입한다.

해당 전략은 다음과 같은 방법으로 진행할 수 있을 듯하다.

## Aim 3. Error-prone PCR 기반 라이브러리 구축

### 목적

HispS 및 NpgA의 다양한 변이 라이브러리를 확보하여,  
E. coli 환경에서 더 잘 작동하는 변이를 선별한다.

### 방법

- NpgA, HispS에 대해 error-prone PCR 수행
- 다양한 돌연변이 포함 라이브러리 확보
- (HispS는 길이가 길어 자연적인 PCR 오류도 변이 다양성에 기여 가능)

하지만, e.coli는 콜로니 단계에서 스크리닝을 통해 활성이 좋은 효소를 가진 클론을 찾기 힘들다. 따라서, 콜로니에서도 활성확인이 가능한 yeast에서 선발하고자 한다.

### 1단계: Yeast에서 라이브러리 스크리닝

- TAR cloning 등을 활용한 조합 라이브러리 구축
- 발광 강도 기반 선별
- 강·약 클론 분리

고려해야할 점:

> Yeast에서 강한 클론이 E. coli에서도 최적이라는 보장은 없다.

---

### 2단계: E. coli에서 재확인

- Yeast에서 선별한 강·약 클론을 E. coli에 도입해서 강도가 유사하게 유지되는 지 확인이 필요
- 발현 및 발광 재검증
- E. coli 최적화 클론 선별

---

## 추가 확장 아이디어

만약 전체 경로 발현이 과도한 burden이라면:

- npgA + hisps만 가진 클론 우선 평가
- Hispidin이 세포 외로 분비된다는 전제 하에
- h3h + luz 클론과 co-culture 실험 수행
- caffeic acid 처리 후 발광 확인

---

# 3. 기대 효과

- PKS의 적정 발현 강도 범위 규명
- E. coli에 최적화된 효소 변이 확보
- 합성생물학 기반 히스피딘 생산 시스템 확립

