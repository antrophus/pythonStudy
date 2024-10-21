#0.import
import mysql.connector
from mysql.connector import Error

# name = input("이름을 입력하세요: ")
# hp = input("번호를 입력하세요: ")
# company = input("회사번호 입력하셍: ")


try:
    #1.연결/컨넥션 얻기
    conn = mysql.connector.connect(
        host="localhost",
        user="phonebook",
        password="phonebook",
        database="phonebook_db"
    )
    print("연결 성공")

    #2.커서생성
    cursor = conn.cursor()
    #3.SQL문준비  / 바인딩 / 실행
    #--SQL문
    query = """
        select person_id,
                name,
                hp,
                company
        from	person
    """

    #--바인딩(튜플)

    #--실행
    cursor.execute(query)
    resultset = cursor.fetchall()

    #4.결과처리 리스트[(튜플), (튜플), (튜플)]
    person_list = []
    for row in resultset:
        person_vo = {
            "person_id": row[0],    # person_id
            "name": row[1],         # name
            "hp": row[2],           # hp
            "company": row[3]       # company
        }
        person_list.append(person_vo)
    print(person_list)
    print(person_list[0]["name"])   # 파라미터로 꺼내기는 "문자열"로 꺼낸다.
except Error as e:
    print(f"데이터베이스 오류: {e}")

finally:
    #5.자원정리
    if conn is not None:
        conn.close()

    if cursor is not None:
        cursor.close()