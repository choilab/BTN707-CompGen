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
  - Input으로 fastq(paired), fna(index, align)를 받을 때 Output으로 bam 파일을 생성함.
  - 웹에 제공할 파일로, trimming report, bam, aligned log 제공 가능.
+ 보완할 점
  - Gene count table을 만들어야함. (Linux의 Featurecount와, R의 edgeR 중 선택할 것.)
  - script의 각 부분을 함수로 정의해 옵션(아래 기술함)에 따라 선택적으로 구동되게 해야함.
    - 옵션 1 : Model animal의 경우, indexing과정을 불필요하게 미리 만들어놓은 index를 읽도록 함.
    - 옵션 2 : one-way 옵션을 추가
    - 옵션 3 : 여러 사용자가 사용할 경우에 대한 대비(쓰레드 분배, 사용자 별 디렉토리 설정) 
   - Pair인데, pairing이 되지 않거나, fna, gff 파일이 올라오지 않을 경우 에러메세지 표시
 
#### Progress 2 : Simple file upload web app by django
+ 간단하게 web에 upload한 파일들이 leafeon 서버에 저장되는 django script를 만듦 [codes](https://github.com/choilab/BTN707-CompGen/tree/main/2022-fall/jjpark/Supplementary%20data/week2_upload_webapp)
+ 스크립트 진행 상황
  - 사용자가 여러 파일을 업로드하면, 메모리에 저장된 파일들을 디렉토리에 쓰는 방식으로 구동되는 웹 앱을 생성함.

+ 보완할 점
  - 여러 파일을 업로드 할 때, 구동방식의 문제로 시간이 오래 걸림.
  - 이용자가 많을 경우, 여러 파일을 동시에 수송하기 힘듦.
  - 옵션을 추가적으로 생성하지 못하고, 단순히 업로드만 구현됨.
