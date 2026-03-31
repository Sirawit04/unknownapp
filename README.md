# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram
<img width="768" height="1001" alt="image" src="https://github.com/user-attachments/assets/29112e86-ea2a-4ab9-8fdb-37d13f7ebc60" />


### Flowchart of the main workflow
```mermaid
flowchart TD
    Start --> LoginMenu

    LoginMenu -->|1| StudentLogin
    LoginMenu -->|2| AdminLogin
    LoginMenu -->|3| Exit

    %% Student Flow
    StudentLogin --> StudentMenu

    StudentMenu -->|1| ViewCatalog
    StudentMenu -->|2| RegisterCourse
    StudentMenu -->|3| DropCourse
    StudentMenu -->|4| ViewSchedule
    StudentMenu -->|5| Billing
    StudentMenu -->|6| EditProfile
    StudentMenu -->|7| Logout

    Logout --> LoginMenu

    %% Admin Flow
    AdminLogin --> AdminMenu

    AdminMenu -->|1| ViewCatalog
    AdminMenu -->|2| ViewRoster
    AdminMenu -->|3| ViewStudents
    AdminMenu -->|4| AddStudent
    AdminMenu -->|5| EditStudent
    AdminMenu -->|6| AddCourse
    AdminMenu -->|7| EditCourse
    AdminMenu -->|8| ViewScheduleAdmin
    AdminMenu -->|9| BillingAdmin
    AdminMenu -->|10| LogoutAdmin

    LogoutAdmin --> LoginMenu

    Exit --> End
```

### Prompts
Convert a Java course registration function into Python, including enroll and drop course logic.

Write a simple Python CLI program that allows a student to:
- view courses
- register for a course
- drop a course

Ensure the program includes:
- capacity checking
- prevention of duplicate enrollment
- simple menu interaction
