export default function createReportObject(employeesList) {
  const myObj = {};
  myObj.allEmployees = { ...employeesList };
  myObj.getNumberOfDepartments = () => Object.keys(myObj).length;
  return myObj;
}
