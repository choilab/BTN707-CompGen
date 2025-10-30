#!/bin/bash
set -e # 스크립트 실행 중 오류 발생 시 즉시 중단

echo "--- 1단계: 유전체 다운로드 및 준비 ---"

# 유전체 다운로드 및 압축 해제
datasets download genome taxon "Lactiplantibacillus plantarum" --assembly-source all --filename L_plantarum_genomes.zip
unzip -o L_plantarum_genomes.zip -d data/genomes/ # -o 옵션으로 덮어쓰기 허용

# 최종 파일 개수 확인
GENOME_COUNT=$(ls data/genomes/*.fna | wc -l)
echo "다운로드 완료: 총 ${GENOME_COUNT}개의 유전체 파일 확인"
echo ""


echo "--- 2단계: SKANI All-vs-All ANI 계산 ---"

# 변수 설정
GENOME_DIR="data/genomes"
OUTPUT_DIR="results"
SKANI_OUTPUT="${OUTPUT_DIR}/skani_raw_output.txt"
THREADS=16

# 결과 디렉터리 생성
mkdir -p ${OUTPUT_DIR}

# skani 실행 (conda 환경에서 실행 필요)
# conda install -c bioconda skani
skani triangle ${GENOME_DIR}/*.fna \
    -o ${SKANI_OUTPUT} \
    -t ${THREADS} \
    -s 80

echo "SKANI 분석 완료. 결과 파일: ${SKANI_OUTPUT}"
echo "--- 작업 완료 ---"