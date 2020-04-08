# Python Type Checking(Guide) -- 20200408
- Reference: https://realpython.com/python-type-checking/

## Contents
```
1. Type Systems
  1-1 Dynamic Typing
  1-2 Static Typing
  1-3 Duck Typing
2. Hello Types
3. Pros and Cons
4. Annotations
  4-1 Function Annotations
  4-2 Variable Annotations
  4-3 Type Comments
  4-4 So, Type Annotations or Type Comments?
5. Playing With Python Types, Part 1
  5-1 Example: A Deck of Cards
  5-2 Sequences and Mappings
  5-3 Type Aliases
  5-4 Functions Without Return Values
  5-5 Example: Play Some Cards
  5-6 The Any Type
6. Type Theory
  6-1 Subtypes
  6-2 Covariant, Contravariant, and Invariant
  6-3 Gradual Typing and Consistent Types
7. Playing With Python Types, Part 2
  7-1 Type Variables
  7-2 Duck Types and Protocols
  7-3 The Optional Type
  7-4 Example: The Object(ive) of the Game
  7-5 Type Hints for Methods
  7-6 Classes as Types
  7-7 Returning self or cls
  7-8 Annotating *args and **kwargs
  7-9 Callables
  7-10 Example: Hearts
8. Static Type Checking
  8-1 The Mypy Project
  8-2 Running Mypy
  8-3 Adding Stubs
  8-4 Typeshed
  8-5 Other Static Type Checkers
  8-6 Using Types at Runtime
9. Conclusion
```


## Object
```
- Type annotations and type hints
  · 타입에 대한 주석과 힌트
- Adding static types to code, both your code adn the code of others
  · 모든 코드에 정적 타입 추가
- Running a static type checker
  · 정적 타입 체커 실행
- Enforcing types at runtime
  · 런타임에 타입 적용
```

## 1. Type Systems
모든 프로그래밍 언어는 각 각의 다른 타입 시스템을 포함하고 있다.

### 1-1. Dynamic Typing
Python은 동적 타입 언어이다. 
이것은 Python 인터프리터가 오직 코드가 실행 될 때 타입 체킹을 한 다는 것과 실행 시간 동안 변수의 타입이 변경 될 수 있음을 의미한다.
다음의 예가 Python의 동적 타입을 증명한다

```
if False:
    1 + "two"  # This line never runs, so no TypeError is raised
else:
    1 + 2
# result: 3

1 + "two"  # Now this is type checked, and a TypeError is raised
# result: TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

첫 번째 예에서 1 + "two"가 절대 실행되지 않으면 절대 타입은 체크되지 않는다.
두 번째 예에서 Python에서 당신은 integer형과 string형을 결합할 수 없으므로, 1 + "two"가 실행될 때 TypeError가 발생된다.

다음으로, 변수가 타입을 변경 할 수 있는지 알아보자.

```
thing = "Hello"
print(type(thing))
# result: <class 'str'>

thing = 28.1
print(type(thing))
# result: <class 'float'>
```

type()은 객체의 타입을 반환한다.
이 예에서 thing의 타입은 변경 될 수 있음을 확인 할 수 있으며, Python은 정확하게 타입이 변경 되었음을 인지한다.

### 1-2. Static Typing
정적 타입은 동적 타입과 정반대 되는 개념이다.
정적 타입은 프로그램이 실행되지 않아도 타입 체킹이 수행된다.
C와 Java 같은 정적 타입 언어들은 당신의 프로그램이 컴파일 될 때 타입 체킹이 수행된다.

비록 다른 타입의 변수를 캐스팅하는 메커니즘이 있을 수 있으나 정적 타입에서 변수들은 일반적으로 타입이 변경되지 않는다.

정적 타입 언어의 간단한 예제를 살펴보자. 다음은 Java 코드의 한 부분이다.
```
String thing;
thing = "Hello";
```

첫 번째 줄은 컴파일 시 thing이라는 이름의 변수가 String 타입으로 바인딩 되었음을 선언하였다.
해당 변수는 다른 타입으로 결코 재 바인딩 될 수 없다.
두 번째 줄에서 thing은 값을 할당 받았다.
이것은 String 객체 외의 값들이 절대 선언될 수 없다.
예를 들어서 만약 당신이 thing = 28.1f으로 선언하면 컴파일러는 양립될 수 없는 타입 때문에 에러를 발생시킬 것이다.

Python은 항상 동적으로 타이핑 된 언어로 남을 것이다.
하지만, PEP 484는 Python 코드에서도 정적 타입 체킹을 가능하도록 하는 type hints를 소개한다.

대부분의 정적 타입 언어들에서 타입이 작동하는 방식과 달리, type hints는 스스로 Python이 타입을 강제하도록 하는 것은 아니다. 이름에서 알 수 있듯이 type hints는 단지 타입을 제안한다.
type hints를 활용한 정적 유형 검사를 수행하는 다른 도구들을 나중에 소개하도록 하겠다.


### 1-3. Duck Typping(다른 설명으로 대체함)
Python에 대해 이야기 할 때 자주 쓰이는 또 다른 용어는 Duck Typing이다.
이 용어는 "오리처럼 걷고 오리처럼 꽥꽥거리면 오리임에 틀림없다"는 말에서 유래되었다.
객체가 실행이 된 시점에서 해당 method와 attribute를 확인하여 객체의 타입을 확인한다.
덕 타이핑(Duck Typing)이란?

```
class Duck:
    def quack(self):
        print('꽥꽥')

    def feathuers(self):
        print('오리에게 흰색, 회색 깃털이 있습니다.')

    def fly(self):
        print('오리가 날았지만 곧 떨어집니다.')


class Person:
    def quack(self):
        print('이 사람이 오리를 흉내냅니다.')

    def feathuers(self):
        print('사람은 바닥에서 깃털을 주어서 보여줍니다.')


def in_the_forest(duck):
    duck.quack()
    duck.feathuers()
    duck.fly()


def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)


if __name__ == "__main__":
    game()

# result:
# 꽥꽥
# 오리에게 흰색, 회색 깃털이 있습니다.
# 오리가 날았지만 곧 떨어집니다.
# 이 사람이 오리를 흉내냅니다.
# 사람은 바닥에서 깃털을 주어서 보여줍니다.
# AttributeError: 'Person' object has no attribute 'fly'
```

class Duck과 Person은 quack()와 feathuers()의 동일 method를 가지고 있지만.
Person class의 경우 fly() method를 가지고 있지 않기 때문에 AttributeError가 발생한다.

이러한 duck typing의 경우 타입에 대해 매우 자유롭게 작성 할 수 있다.
하지만 코드 실행 시 자료형 오류나 선언되지 않은 method나 attribute를 찾지 못해 오류가 발생할 수 있다. 이러한 문제들은 개발이 어느 정도 진행 된 뒤 발생 될 가능성이 크며, 해당 오류를 찾는 것이 쉽지 않다.



## 2. Hello Types
이번 장에서는 type hints를 function에 어떻게 추가 하는지 알아 볼 것이다.
다음의 function은 첫 글자를 대문자화 해주고 장식 라인을 추가하여 텍스트 문자열을 헤드라인 형태로 바꾼다.

```
def headline(text, align=True):
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else: 
        return f" {text.title()} ".center(50, "o")

print(headline("python type checking"))
# result: 
# Python Type Checking
# --------------------

print(headline("python type checking", align=False))
# oooooooooooooo Python Type Checking oooooooooooooo
```

해당 function은 기본적으로 밑줄과 왼쪽 정렬된 헤드라인을 반환한다.
정렬 플래그를 False로 설정하면 o에 감싸져서 중앙에 위치된 헤드라인을 반환하도록 할 수 있다.


function에 대한 타입을 추가하려면 다음과 같이 인수 및 변환 값에 annotation을 달기만 하면 된다.

```
def headline2(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else: 
        return f" {text.title()} ".center(50, "o")
```

text: str 구문은 text 인수는 str 타입이어야 한다고 말한다.
마찬가지로, 선택적 align 인수는 default를 True의 bool 타입을 가져야 한다.
마지막으로, -> str 구문은 headline2()가 문자열을 반환함을 명시하고 있다.

PEP 8은 다음과 같은 구문을 추천한다

  - 
  - 
  - 