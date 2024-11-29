from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb+srv://amitkumarashutosh:amitkumarashutosh@cluster0.pnwrzzb.mongodb.net/')

db = client["ytmanager"]
video_collection = db["videos"]

def list_video():
    print('\n')
    for video in video_collection.find():
        print(f"{video['_id']} | {video['name']} | {video['time']}")
    print('\n')
    print('*' * 50)

def add_video(name, time):
    video_collection.insert_one({'name': name, 'time': time})

def update_video(video_id, name, time):
    video_collection.update_one({'_id': ObjectId(video_id)}, {
        "$set": {'name': name, 'time': time}
    })

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})

def main():
    while True:
        print("\nYoutube Manager | Choose an option")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            list_video()
        elif choice == '2':
            name = input('Enter the video name: ')
            time = input('Enter the video time: ')
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input('Enter the video name: ')
            time = input('Enter the video time: ')
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid input")

if __name__ == '__main__':
    main()
