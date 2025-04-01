from school_schedule.student import Student
import pytest
# Write your tests here!
def test_student_class_instantiation():
    # Arrange
    name = "Quinn"
    grade = "junior"
    classes = [
        "Pre-Calc", 
        "English III", 
        "World History", 
        "Gym", 
        "Chemistry", 
        "Music Composition"
    ]

    # Act
    quinn = Student(name, grade, classes)

    # Assert
    assert name == quinn.name
    assert grade == quinn.grade
    assert classes == quinn.classes
  
def test_add_class():
    # Arrange
    student = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )
    # Act
    new_classes = student.add_class("Art")

    # Assert
    assert "Art" in student.classes
    assert len(student.classes) == 7
    assert new_classes == [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition",
                    "Art"
                  ]

def test_get_num_classes():
    # Arrange
    student = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )
    # Act
    num_classes = student.get_num_classes()

    # Assert
    assert num_classes == 6
    assert len(student.classes) == 6

def test_display_classes():
    #Arrange
    student = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )
    # Act
    class_list = student.display_classes()

    # Assert
    assert class_list == "Pre-Calc, English III, World History, Gym, Chemistry, Music Composition"

def test_summary():
        #Arrange
    student = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )
    # Act
    result_summary = student.summary()

    # Assert
    assert result_summary == "Quinn is a junior enrolled in 6 classes: Pre-Calc, English III, World History, Gym, Chemistry, Music Composition"