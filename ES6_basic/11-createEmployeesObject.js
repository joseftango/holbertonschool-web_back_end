export default function createEmployeesObject(departmentName, employees) {
  const myObj = {};
  myObj[`${departmentName}`] = [...employees];
  return myObj;
}
