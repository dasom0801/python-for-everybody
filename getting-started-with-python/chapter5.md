# CHAPTER 5: 루프와 반복문

## Part1. while 루프

+ 조건이 참이면 while 안의 코드가 실행되고 거짓이면 건너뛴다.
+ 조건이 거짓이 될 때까지 반복한다.
+ 반복 변수의 값을 바꾸지 않으면 무한 루프에 빠지게 된다. 

```python
while n > 0 :
	print(n)
	n = n - 1
print('Blastoff')
print(n)
```

+ break: 루프 종료

  ```python
  while True:
    line = input('> ')
    if line == 'done' :
      break
    print(line)
  print('Done!')
  ```

+ continue:  위로 올라가서 루프 조건을 다시 확인

  ```python
  while True:
      line = input('> ')
      if line[0] == '#' :
          continue
      if line == 'done' :
          break
      print(line)
  print('Done!')
  ```

## Part2. for 루프

+ 유한 루프 

  + 어떤 집합의 원소들에 대해 반복문을 실행하는 것
  + 루프가 실행되는 집합에 따라 유한 번 실행된다. 
  + 반복 변수를 처리할 필요 없음

  ```python
  for i in [5, 4, 3, 2, 1] :
      print(i)
  print('Blastoff!')
  
  friends = ['Joseph', 'Glenn', 'Sally']
  for friend in firends :
      print('Happy New Year:', firend)
  print('Done!')
  ```

## Part3. 반복문

+ for 루프를 이용해 가장 큰 수를 찾아내기

  ```python
  largest_so_far = -1
  print('Before', largest_so_for)
  numbers = [9, 41, 12, 3, 74, 15]
  for the_num in numbers :
      if the_num > largest_so_for :
          largest_so_far = the_num
      print('largest_so_far:', largest_so_far, 'current number:', the_num)
  print('After', largest_so_far)
  ```

  

## Part4. 반복문 응용

+ `None` 자료형 : 값이 없다는 것을 의미함

+ `is`와 `is not` 은 변수의 자료형과 값이 동일할 때 True를 반환한다. 자료형 변환은 일어나지 않음. 예) `0 == 0.0` 은 true, `0 is 0.0`은 false

  ```python
  smallest = None
  print('Before')
  numbers = [9, 41, 12, 3, 74, 15]
  for value in numbers:
      if smallest is None:
          smallest = value
      elif value < smallest:
          samllest = value
      print(samllest, value)
  print('After', samllest)
  ```

  

