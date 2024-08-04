# SSAFY_algorithm_study

## Get Started

### 1. 먼저 repository를 fork 합니다.

각자의 github 계정에 코드와 기록이 남을 수 있도록 fork 한 후에 풀이 관리를 합니다.

### 2. 자신의 repository에 있는 **SSAFY_algorithm_study**를 clone합니다.

이제 repository를 clone하여 local에서 관리합니다. 이제부터 자신의 repository에 파일을 관리하듯이 편하게 관리하면 됩니다.

### 4. PR

한 주의 문제를 원본 repsitory에 반영하기 위해 Pull Request를 합니다.

Pull Request는 금요일 스터디가 끝난 후 부터 주말이 끝나기 전까지 진행하고, PR을 생성하면 스터디원이나 장이 확인 후 승인합니다.

### 5. 자신의 repository update

모든 구성원들의 PR에 대한 merge가 완료되면 자신의 repository를 업데이트 합니다.

이를 위해 원본 repsitory와 연결된 upstream이라는 이름의 remote를 만들어줍니다. 이 일은 최초 한 번만 하면 됩니다.

```bash
$ git remote add upstream https://github.com/qja1998/SSAFY_algorithm_study.git
$ git remote -v // check
```

remote가 정상적으로 연결되었다면 업데이트 합니다. 업데이트는 다음와 같은 단계로 진행됩니다.

1. fetch로 원본을 변셩사항 내려받기
2. 내려받은 변경사항을 내 local repository와 merge
3. merge한 내용을 내 원격 저장소에 반영

```bash
$ git fetch upstream // 원본의 변경사항 내려받기
$ git merge upstream/main // 내려받은 변경사항을 나의 repository와 merge
$ git push origin main // 내 원격 저장소에 반영
```

## Directory Tree

```bash
├───BOJ
└───SWEA
    ├───D1
    ├───D2
    ├───D3
    ├───D4
    │   ├───1210_Ladder1
    │   ├───1225_암호생성기
    │   ├───1226_미로1
    │   └───1231_중위순회
    ├───D5
    └───모의_역량_테스트
        ├───1767_프로세서_연결하기
        └───4008_숫자_만들기
```

문제 사이트 -> 문제 난이도 -> 문제 디렉토리로 이어지는 구조입니다.

문제 디렉토리 안에 문제가 `.MD` 파일로 저장되며, 해당 폴더에 자신 이름의 python 파일을 업로드 합니다.