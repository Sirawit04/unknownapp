# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram
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

### Flowchart of the main workflow

### Prompts
