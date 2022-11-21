# Weekly Report
## Week 2 (11/15 ~ 11/22)
### Goal 
+ Django tutorial 
+ Upload application implementation
+ Pipeline for stored fastq format file 

### Progress
#### Progress 1 : Pipeline script
+ Pipeline [script](https://github.com/choilab/BTN707-CompGen/blob/main/2022-fall/jjpark/Supplementary%20data/pipeline.py)
+ 스크립트 진행 상황
  - Input으로 FASTQ(paired), FNA(index, align)를 받을 때 Output으로 bam 파일을 생성함.
  - 웹에 제공할 파일로, trimming report, bam, aligned log 제공 가능.
+ 보완할 점
  - Gene count table을 만들어야함. (Linux의 Featurecount와, R의 edgeR 중 선택할 것.)
  - script의 각 부분을 함수로 정의해 옵션(아래 기술함)에 따라 선택적으로 구동되게 해야함.
    - 옵션 1 : Model animal의 경우, indexing과정을 불필요하게 미리 만들어놓은 index를 읽도록 함.
    - 옵션 2 : paired FASTQ 옵션을 추가
    - 옵션 3 : 여러 사용자가 사용할 경우에 대한 대비(쓰레드 분배, 사용자 별 디렉토리 설정) 
