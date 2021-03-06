# CHAPTER 3: 조건부 실행

## Part 1. 조건문

+ if
  + 질문이 참이면 실행되고 아니면 스킵
+ 비교연산자
  + <, <= , == , >=, >, !=
+ 들여쓰기
  + 파이썬에서는 들여쓰기를 잘못하면 에러가 발생한다.
  + 들여쓰기를 하면 같은 블로에 있는 이상 뜰여쓰기를 유지해야 한다.
  + 탭과 스페이스를 제대로 구분하지 않으면 들여쓰기 에러 발생

## Part2. 조건문(elif)과 예외처리(try, except)

+ elif

  + 여러개의 갈래 중 하나를 고르는 것
  + 순서에 따라 조건을 확인한다. 순서가 중요함

+ try/except

  + 확실히 traceback 에러가 나서 프로그램이 중단될 부분을 안다면 중단되는 것을 원치 않을 것 

  + 사용자의 입력값을 보고 코드에서 프로그램이 중단 될 수 있는 부분을 예상하고 해결 할 수 있어야 한다

  + 중단 될 수 있는 코드를 `try`로 감싸면 실패할 수 있으니 실패하면 `except`를  실행하라는 의미

  + `except`가 실행되면 다시 `try`로 돌아가지 않는다. 생략되는 코드 발생

    ```python
    astr = 'Hello Bob'
    istr = int(astr) 
    # 문자를 정수로 바꿀 수 없다 > 에러발생 > 프로그램이 멈춘다
    
    #try/except 적용
    astr = 'Hello Bob'
    try:
        istr = int(astr)
    except:
        istr = -1
    #에러가 발생하면 except를 실행, 문제가 없다면 except는 무시된다. 
    ```

    