# LOGO interpreter

# 문제
# - 로고 언어를 해석하는 인터프리터를 작성합니다
# - 얻어야 하는 결과물은 출발지로부터 떨어진 직선거리를 구하는 것입니다

# 로고 문법
# - 명령은 두가지가 존재합니다.
#   - fd: 단위 거리만큼 앞으로 전진
#   - rt: 단위 각도만큼 시계방향 회전
# - 각 명령은 whitespace로 구분되어 연속적으로 명령합니다

# 전제
# - 단위 거리: 1
# - 단위 각도: 90 degree
# - 시작 위치: (0, 0)
# - 시작 방향: 0 degree

# example
# in: "fd rt fd rt fd rt fd"
# out: 0
# in: "fd fd fd rt fd fd fd fd"
# out: 5
# in: "fd rt rt fd fd fd"
# out: 2

# 큰 그림
# 1. 초기 값 세팅
# 1. 위치 [0,0]
# 2. 방향 ->
# 3. 각도 90
# 2. 명령어에 따른 이동
# 1. 공백을 기준으로 분할
# 2. 명령어에 해당하는 함수 생성
# 1. fd : 바라보는 방향으로 전진
# 2. rt : 만들어진 방향 셋에 대해 회전
# 3. 명령 실행
# 3. 결과 값 산출
# 1. 피타고라스에 의한 결과값 산출

def LOGO_interpreter(commands):
    # 1. 세팅
    init_position = [0, 0]
    position = [0, 0]
    rotation = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    current_rotate = 0

    # 2. 명령어 수행
    commands = commands.split()

    def fd_function(current_rotate):
        position[0] += rotation[current_rotate][0]
        position[1] += rotation[current_rotate][1]

    def rt_function(current_rotate):
        return (current_rotate + 1) % 4

    # O(N)
    def process_commands(commands, current_rotate):
        for command in commands:
            if command == "fd":
                fd_function(current_rotate)
            elif command == "rt":
                current_rotate = rt_function(current_rotate)

    process_commands(commands, current_rotate)

    # 3. 최종 결과 산출
    def make_distance(target, current):
        return ((current[0] - target[0]) ** 2 + (current[1] - target[1]) ** 2) ** 0.5

    result = make_distance(init_position, position)

    return result


class Assert:
    def __init__(self, func):
        self.func = func

    def assert_function(self, expected, *args):
        return self.func(*args) == expected


interpreter_assert = Assert(LOGO_interpreter)


# print(interpreter_assert.assert_function(5, "fd fd fd rt fd fd fd fd"))

# make_distance_assert = Assert(make_distance)
# print(make_distance_assert.assert_function(2.0, [1, 0], [3, 0]))


class LOGOInterpreter:
    rotation = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def __init__(self, commands):
        self.commands = commands.split()
        self.init_position = [0, 0]
        self.position = [0, 0]
        self.current_rotate = 0

    def process_commands(self):
        for command in self.commands:
            if command == "fd":
                self.fd_function()
            elif command == "rt":
                self.current_rotate = self.rt_function()
        result = self.make_distance(self.init_position, self.position)
        return result

    def fd_function(self):
        self.position[0] += self.rotation[self.current_rotate][0]
        self.position[1] += self.rotation[self.current_rotate][1]

    def rt_function(self):
        return (self.current_rotate + 1) % 4

    def make_distance(self, target, current):
        return ((current[0] - target[0]) ** 2 + (current[1] - target[1]) ** 2) ** 0.5


logo_interpreter = LOGOInterpreter("fd fd fd rt fd fd fd fd")
print(logo_interpreter.process_commands())