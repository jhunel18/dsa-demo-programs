int count = 0
List<StudentDB> students = new List<StudentDB>();
StudentInformationEntity = studentInfo = new StudentInformationEntity();

//Assume here tha I already connected to db and the stored procedure

if(!row.HasRows){
    return listStudentInfo
}
while(row.Read()){
    if count == 0{
        tripInfo.FD = ((((dataReader)row)["DC"]== null)?string.Empty : ((dataReader)row)["DC"].ToString());
        tripInfo.FN = ((((dataReader)row)["FN"]== null)?string.Empty : ((dataReader)row)["FN"].ToString());
        tripInfo.FC = ((((dataReader)row)["FC"]== null)?string.Empty : ((dataReader)row)["FC"].ToString());
        tripInfo.TC = ((((dataReader)row)["TC"]== null)?string.Empty : ((dataReader)row)["TC"].ToString());
        tripInfo.AcRN = ((((dataReader)row)["TNo"]== null)?string.Empty : ((dataReader)row)["TNo"].ToString());
        tripInfo.AT = string.Empty;
        tripInfo.AcT = ((((dataReader)row)["AcT"]== null)?string.Empty : ((dataReader)row)["AcT"].ToString());
        tripInfo.Dest = ((((dataReader)row)["Dest"]== null)?string.Empty : ((dataReader)row)["Dest"].ToString());
        tripInfo.Arr = ((((dataReader)row)["Arr"]== null)?string.Empty : ((dataReader)row)["Arr"].ToString());
        trinpInfo.PLoad = string.Empty;
        c++;
    }
    StudentDB studentDB = studentDB();
    studentDB.AcTQ = string.Empty;
    studentDB.Bs = ((((dataReader)row)["Bs"]== null)?string.Empty : ((dataReader)row)["Bs"].ToString());
    studentDB.CID = ((((dataReader)row)["EmpNumber"]== null)?string.Empty : ((dataReader)row)["EmpNumber"].ToString());
    studentDB.Name = ((((dataReader)row)["EmpName"]== null)?string.Empty : ((dataReader)row)["EmpName"].ToString());
    studentDB.Name = ((((dataReader)row)["EmpName"]== null)?string.Empty : ((dataReader)row)["EmpName"].ToString());
}
    studentInfo.StudentSub = studentSub;
    listStudentInfo.Add(studentInfo)
}


return db.executeSP({
    'name':'sp_getStudent',
    'database':'sis_db',
    'query':{
        "id":id,
        "name":name
    }
})
.then(data=>{
    if(!data.length){
        return flightInfo;
    }
})

const structuredData = data.map(item=>{
    const structuredItem = {
        "classCode":item.classCode,
        "classRoom":item.classRoom,
        "students":[{
            "studentName":item.studentName,
            "studentAddress":item.studentAddress
        }]
    } return structuredItem;
}) return structuredData;