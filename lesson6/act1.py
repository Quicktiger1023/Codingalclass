camera=1
microphone=5
storage=7
location=4

apps=[
    "math app",
    "sst app",
    "reading app",
]

name=int(input("enter your name:    ")).lower()
application=int(input("enter the application you want to access:    ")).lower()

if type(name) is st:
    print("the student name is stored as text")
if type(apps) is not st:
    print("the student name is  not stored as text")

if apps in application:
    print(application,"is not in the restricted list")
else:
    print(application,"is in the restricted list")

apps1=[
    "gaming apps",
    "social media",
    "shopping apps",
]
if application not in apps1:
    print(application,"is not in the restricted list")
else:
    print("ACCESS DENIED: APP IS FORMALLY RESTRICTED")