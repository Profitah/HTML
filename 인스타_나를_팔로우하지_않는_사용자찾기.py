import json
import os

# 파일 경로 설정
followers_file_path = '파일 경로 입력'  
following_file_path = '파일 경로 입력'

# 파일을 찾을 수 없을 때
if not os.path.exists(followers_file_path):
    print(f"경로에 파일이 존재하지 않습니다: {followers_file_path}")
if not os.path.exists(following_file_path):
    print(f"경로에 파일이 존재하지 않습니다: {following_file_path}")

# 데이터 전처리  :  팔로잉 목록과 팔로워 목록을 set으로 저장
# 팔로워 목록 전처리
followers = set()  # 초기화
try:
    with open(followers_file_path, 'r') as file: # 파일 불러오기
        followers_data = json.load(file) 
        for dic_followers in followers_data: # 딕셔너리 형태로 저장된 팔로워 데이터를 순회
            if 'string_list_data' in dic_followers: # 조건 : string_list_data 키가 있는 경우
                for followers_info in dic_followers['string_list_data']: # string_list_data 키에 넣은 딕셔너리 value 값들을 순회
                    followers.add(followers_info['value'])  # followers set에 value(팔로워 인스타그램 아이디) 추가
            else:
                print("팔로워 데이터에서 string_list_data 키를 찾을 수 없습니다. 파일을 다시 확인해주세요.") # 예외처리 1 : string_list_data 키가 없는 경우
except Exception as error :# 예외처리 2 : 그 밖의 모든 에러
    print(f"팔로워 목록을 불러오던 중 에러가 발생했습니다. 해결해주세요. {error}") 

# 팔로잉 목록 전처리
following = set()  # 초기화
try:
    with open(following_file_path, 'r') as file: # 파일 불러오기
        following_data = json.load(file)

        # relationships_following(사용자 아이디)만 추출하기
        if 'relationships_following' in following_data: # 조건 : relationships_following 키가 있는 경우
            for dic_followers in following_data['relationships_following']: # relationships_following 키에 넣은 딕셔너리 value 값들을 순회
                if 'string_list_data' in dic_followers: # 조건 : string_list_data 키가 있는 경우
                    for entry in dic_followers['string_list_data']: # string_list_data 키에 넣은 딕셔너리 value 값들을 순회
                        following.add(entry['value'])  # following set에 value(팔로잉 인스타그램 아이디) 추가
        else:
            print("팔로잉 데이터에서 relationships_following 키를 찾을 수 없습니다. 파일을 다시 확인해주세요.") # 예외처리 1 : relationships_following 키가 없는 경우
except Exception as error: # 예외처리 2 : 그 밖의 모든 에러
    print(f"팔로잉 목록을 불러오던 중 에러가 발생했습니다. 해결해주세요. {error}") 

# 나를 팔로우하지 않는 사용자 찾기
unfollowers = following - followers  # 내 팔로잉 목록에는 있지만, 팔로워 목록에는 없는 사용자 찾기

# 결과 출력
print("나를 팔로우 하지 않는 사용자 목록:", unfollowers)
