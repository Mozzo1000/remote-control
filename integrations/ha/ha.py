import os
from connection import Connection
from states import StateList
from dotenv import load_dotenv

load_dotenv()

def main():
    conn = Connection(os.environ.get("HOME_ASSISTANT_URL"), os.environ.get("HOME_ASSISTANT_API_TOKEN"))
    print(conn.api_status())
    print(conn.components())
    #state_list = StateList(conn)
    #print(state_list.all())

if __name__ == "__main__":
    main()