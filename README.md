# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram
```mermaid
graph TD
    User((User))

    User --> StudentLogin[Login as Student]
    User --> AdminLogin[Login as Admin]

    %% Student use cases
    StudentLogin --> ViewCatalog[View Course Catalog]
    StudentLogin --> RegisterCourse[Register for Course]
    StudentLogin --> DropCourse[Drop Course]
    StudentLogin --> ViewSchedule[View Schedule]
    StudentLogin --> Billing[View Billing Summary]
    StudentLogin --> EditProfile[Edit Profile]

    %% Admin use cases
    AdminLogin --> ManageCourses[Add/Edit Course]
    AdminLogin --> ManageStudents[Add/Edit Student]
    AdminLogin --> ViewRoster[View Class Roster]
    AdminLogin --> ViewAllStudents[View All Students]
    AdminLogin --> AdminBilling[View Student Billing]
```

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
```mermaid
flowchart TD

A([Start]) --> B[Print Banner & Load Data]

B --> C{Login Menu}

C -->|1. Student| D[Student Login]
C -->|2. Admin| E[Admin Login]
C -->|3. Exit| F[Save Data & Exit]

D --> G{Student Menu}

G -->|1 View Catalog| G
G -->|2 Register Course| G
G -->|3 Drop Course| G
G -->|4 View Schedule| G
G -->|5 Billing Summary| G
G -->|6 Edit Profile| G
G -->|7 Logout| C

E --> H{Admin Menu}

H -->|1 View Catalog| H
H -->|2 View Roster| H
H -->|3 View Students| H
H -->|4 Add Student| H
H -->|5 Edit Student| H
H -->|6 Add Course| H
H -->|7 Edit Course| H
H -->|8 View Schedule| H
H -->|9 Billing Summary| H
H -->|10 Logout| C

F --> I([End])
```
### Prompts
