export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((obj) => obj.location === city)
    .map((student) => {
      const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);

      return {
        ...student,
        grade: matchingGrade ? matchingGrade.grade : 'N/A',
      };
    });
}
