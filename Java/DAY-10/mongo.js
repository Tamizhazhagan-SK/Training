console.log("DB connected");
let username = "Alex";
console.log("Name: " + username);

/*
MongoBD - create collection
*/

db.createCollection("employee"); 

/*
in NoSQL, _id must be mandatorily entered. if not, system will generate on its own.
it follows an ObjectID - hexa decimal values
*/ 

//inserting the documents
db.employee.insertOne({name: "Alex", salary:45000});
db.employee.insertOne({name: "Alex", salary:35000});
db.employee.insertOne({name: "Brad Pitt", salary:55000, phone:9876543210});
db.employee.insertOne({username: "Tom Cruise", password:"user@123"});
db.employee.insertOne({_id:12, username: "Tom Cruise", password:"user@123"});

db.employee.insertOne({_id:1,name: "Nolan", salary:45000});
db.employee.insertOne({_id:2,name: "Robert", salary:55000});
db.employee.insertOne({_id:3,name: "Tom", salary:65000});
db.employee.insertOne({_id:4,name: "Matt", salary:75000});
db.employee.insertOne({_id:13,name: "Matt", salary:75000});




//retrieving the documents
db.employee.find();

console.log("================================================================")

db.employee.find({_id:12});

console.log("================================================================")

/*
to find more documents with other parameters:
$gt,  $lt,  $gte, $or,  $and, $regex
*/

// db.employee.find({salary: {$gt:60000}});


console.log("====================using $or and $and=========================")

console.log("====================using $and=========================")

db.employee.find({$and:[{username:"Tom Cruise"}, {password:"1234"}]}); //when using $and, both should be true

console.log("====================using $or=========================")

db.employee.find({$or:[{username:"Tom Cruise"}, {password:"1234"}]}); //when using $or, any one can be true

console.log("====================using insertMany=========================")
db.employee.insertMany([{_id:5,name: "Will", salary:85000},{_id:6,name: "Mark", salary:95000},{_id:7,name: "Cooper", salary:105000},{_id:8,name: "Josh", salary:115000}]);


console.log("====================using find=========================")
// retrieving between data
// db.employee.find({salary: {$lt:60000,$gte:30000}});


console.log("====================Sorting in ascending order : 1=========================")
db.employee.find({salary:{$exists:true}}).sort({salary:1});

console.log("====================Sorting in descending order : -1=========================")
db.employee.find({salary:{$exists:true}}).sort({salary:-1});


console.log("====================using count=========================")
db.employee.find().count();


console.log("====================using find with parameters=========================")
db.employee.find({name:"Alex"});


//updating a single documents - updateOne({filter},{expression})
console.log("====================using updateOne with values=========================")
db.employee.updateOne({name:"Alex"},{$set:{salary:9999999999}});

console.log("====================using updateOne after updation=========================")
db.employee.find({name:"Alex"});

//delete single documents - deleteOne({filter})
console.log("====================using deleteOne with values=========================")
db.employee.deleteOne({name:"Alex"});

console.log("====================using deleteOne after updation=========================")
db.employee.find({name:"Alex"});

//delete mulitple documents - deleteMany({filter})
console.log("====================using deleteMany with values=========================")
db.employee.deleteMany({name:"Matt"});

console.log("====================using deleteMany after updation=========================")
db.employee.find({name:"Matt"});
console.log("all matching records deleted");

//passing data in collections
console.log("================================================================")

db.createCollection("students");

db.students.insertMany([
  {_id:10, name:"Akon", email:"akon123@gmail.com", dob: new ISODate("2002-10-20")},
  {_id:20, name:"Bieber", email:"bieber123@gmail.com", dob: new ISODate("2002-09-19")},
  {_id:30, name:"Coldplay", email:"coldplay123@gmail.com", dob: new ISODate("2002-08-18")}
]);

console.log("=====================Finding all students======================")
db.students.find();

function printStudents() {
  let students = db.students.find().toArray();
  students.forEach((item, index) => {
    console.log((index + 1) + ". " + item.name);
  });
}

printStudents();


console.log("=====================activity: printing the masked email======================")



function maskEmail(email) {
    let [username, domain] = email.split("@");
    let maskedUsername = username.charAt(0) + "***" + username.slice(-3);
    return maskedUsername + "@" + domain;
}

function printStudentEmails() {
    let students = db.students.find().toArray();
    students.forEach((student, index) => {
        console.log((index + 1) + ". " + student.name + ": " + maskEmail(student.email));
    });
}

printStudentEmails();













console.log("All systems online");