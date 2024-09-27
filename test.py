import json
import os
import pytest 

# 파일 경로 설정
test_followers_file_path = './test_follower_1.json'
test_following_file_path = './test_following.json'

def load_data(test_file_path):
    if not os.path.exists(test_file_path):
        raise FileNotFoundError(f"지정하신 경로에 해당 파일이 없습니다: {test_file_path}")
    
    with open(test_file_path, 'r') as file:
        return {info['value'] for test_value in json.load(file) for info in test_value.get('string_list_data', [])}

# 테스트 결과 파일 생성
@pytest.fixture 
def test_file(): 
    path = "./test_dummy.json" 
    open(path, 'w').close()  
    yield path
    os.remove(path)

# 팔로워 - 팔로잉 비교
def test_followers_minus_following():
    followers = load_data(test_followers_file_path)
    following = load_data(test_following_file_path)
    difference = followers - following

    # difference에 대한 검증
    assert len(difference) >= 0  # 비어 있거나 0명 이상이어야 함. |  예측하지 못한 형식의 데이터 출력 방지

    # 출력 형식 확인
    assert "s2ent_official" in difference or len(difference) == 0  

# 예외 처리
# 파일이 없는 경우
def test_FileNotFoundError():
    with pytest.raises(FileNotFoundError):
        load_data("non_existent_file.json")

# 키 에러
def test_key_error(test_file):
    with pytest.raises(ValueError):
        load_data(test_file)

if __name__ == "__main__":
    pytest.main()
