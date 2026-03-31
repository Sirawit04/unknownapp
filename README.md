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

### Prompts
