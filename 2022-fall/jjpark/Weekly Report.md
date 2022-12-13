# Weekly Report
## Week 2 (11/15 ~ 11/22)
### Goal 
+ Django tutorial 
+ 업로드 기능이 있는 웹 앱 구현
+ 저장된 fastq 파일부터 alignment까지 과정을 한번에 할 수 있는 파이프 라인 설계

### Progress
#### Progress 1 : Pipeline script
+ Pipeline [script](https://github.com/choilab/BTN707-CompGen/blob/main/2022-fall/jjpark/Supplementary%20data/pipeline.py)
+ 스크립트 진행 상황
  - Input으로 fastq(paired), fna(index, align)를 받을 때 Output으로 bam 파일을 생성함.
  - 웹에 제공할 파일로, trimming report, bam, aligned log 제공 가능.
+ 보완할 점
  - Gene count table을 만들어야함.
  - Pair인데, pairing이 되지 않거나, fna, gff 파일이 올라오지 않을 경우 에러메세지 표시
  - script의 각 부분을 함수로 정의해 옵션(아래 기술함)에 따라 선택적으로 구동되게 해야함.
    - 옵션 1 : Model animal의 경우, indexing과정을 불필요하게 미리 만들어놓은 index를 읽도록 함.
    - 옵션 2 : one-way 옵션을 추가
    - 옵션 3 : 여러 사용자가 사용할 경우에 대한 대비( 분배, 사용자 별 디렉토리 설정)  
     
     
   
  <img width="465" alt="image" src="https://user-images.githubusercontent.com/97942772/203237971-a973a158-f2f3-408d-8c3a-318a93be0182.png">
  
  - 보라색 표시 input file, 초록색 표시 output file.
 
#### Progress 2 : Simple file upload web app by django
+ 간단하게 web에 upload한 파일들이 leafeon 서버에 저장되는 django script를 만듦 [codes](https://github.com/choilab/BTN707-CompGen/tree/main/2022-fall/jjpark/Supplementary%20data/week2_upload_webapp)
+ 스크립트 진행 상황
  - 사용자가 여러 파일을 업로드하면, 메모리에 저장된 파일들을 디렉토리에 쓰는 방식으로 구동되는 웹 앱을 생성함.

+ 보완할 점
  - 여러 파일을 업로드 할 때, 구동방식의 문제로 시간이 오래 걸림.
  - 이용자가 많을 경우, 여러 파일을 동시에 수송하기 힘듦.
  - 옵션을 추가적으로 생성하지 못하고, 단순히 업로드만 구현됨.  
  
  

  <img width="785" alt="image" src="https://user-images.githubusercontent.com/97942772/203236730-357880a5-fd7c-4273-aceb-1b439bc10a27.png">
  <img width="785" alt="image" src="https://user-images.githubusercontent.com/97942772/203238881-b7f848c5-a3ed-4abe-b34a-4fdec52746fa.png">
  <img width="785" alt="image" src="https://user-images.githubusercontent.com/97942772/203238113-a28706ef-2932-4da4-ba3b-8fb7ae7fb4f0.png">
  
  - Django를 통한 업로드 사이트와 Zebrafish fastq file을 1/10 크기로 만든 toy fastq file을 업로드 한 결과. 


### Next Week Goal
+ Pipeline의 보완
  - 현재 Pipeline은 gene count table까지 작성하지 못하고, bam 파일까지 작성함. Feature count/countOverlaps 중 하나를 선택해 gene count table을 만들고, GEO2R을 이용한 간단한 통계 이미지 파일을 만드는 것 까지 보완.
+ Pipeline과 업로드 사이트간의 연결 
  - 현재 Pipeline과 web을 통해 저장된 파일들간의 연결이 이뤄지지 못함. Django를 이용한 연결이 필요함. 
+ Web에 Option을 설정하고, Pipeline과 연계
  - 현재 Pipeline은 Paired read에 대해 bam file을 만들고, Model animal에 대한 예외를 적용하지 않음. 추가적인 연구 진행이 필요함.
+ Progress bar 생성
  - 업로드하는 fastq file의 크기가 giga byte 단위기 때문에, Progress bar를 만들고, 업로드가 완료되면 pipeline 구동 버튼을 통한 구동이 필요함. 
+ Counting program의 결정
  - Multi thread를 사용가능한 Linux feature count/subread, R의 countOverlaps중 선택해야함.


## Week 4 (11/29 ~ 12/6)
### Goal 
+ Pipeline의 보완
+ Pipeline과 업로드 사이트간의 연결 

### Progress
#### Progress 1 : Pipeline Update
+ Pipeline을 web service 중인 Leafeon server에서 구동되기 위해 Pipeline의 보완 및 웹과 백엔드 파이프라인의 연결을 실시.
+ 사이트에 Raw file을 업로드 할 시, Trim galore, Hisat indexing, Hisat align까지 구동되어 Leafeon 서버에 파일이 저장됨.
+ bam format file을 웹에서 로컬로 다운로드하는 기능 구현이 필요함.
<img width="785" alt="image" src="https://user-images.githubusercontent.com/97942772/206071543-5b9f757a-5cc0-4faa-9565-e9385b25aa50.png">

  - Input으로 웹에서 paired fastq 파일 2개, reference genome으로 사용할 fna  파일 1개를 넣었을 때, 아웃풋으로 trimmed fastq(.fq), hisat-index 파일, bam 파일이 저장됨.  
+ 소스코드는 [Supplementary data](https://github.com/choilab/BTN707-CompGen/tree/main/2022-fall/jjpark/Supplementary%20data/week4_complete)의 Week4에 저장.

## Week 5 (12/6 ~ 12/13)
### Goal
+ Pipeline 완성
+ Alpha version web service 구동

### Progress
#### Progress 1 : Pipeline Update
+ 이전에 Django를 사용한 Web Application 제작에 UI 가시성이 좋지 않고, 스크립트 작성에 어려움이 있어 Shiny for python으로 구동 프로그램을 변경.
+ Shiny for python에 맞게 Pipeline Update

#### Progress 2 : Web Application Service
+ Input으로 FASTQ (paired only)를 넣어줄 때, quality control, indexing, align까지의 과정을 Leafeon server에서 진행하고, (Thread 12개 사용) 결과물인 BAM format file을 유저가 다운로드 받을 수 있게 구현함.

<img width="785" alt="image" src="https://user-images.githubusercontent.com/97942772/207236845-a3bc3ed6-8fd1-45d6-8ab0-96aa86673117.png">
  - Input으로 로컬에서 웹으로 2개의 paired FASTQ file을 업로드하고, 아웃풋으로 bam파일을 다운로드 받았다.(하단) Reference genome FASTA 파일의 크기가 크기 때문에, 미리 서버에 업로드 하였고, 업로드 된 reference genome의 indexing 및 align의 대상으로 삼는 과정은 버튼을 누르면 구동되게 구현하였다. 
 
 + 소스코드는 [Supplementary data](https://github.com/choilab/BTN707-CompGen/tree/main/2022-fall/jjpark/Supplementary%20data/week5_shiny_try3/my_app)에 저장.
 + Service URL : http://leafeon.korea.ac.kr:8001/
