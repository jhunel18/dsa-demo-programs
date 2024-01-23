var training = trainingDates.OrderByDescending(td=>td.DateFrom).First.training;
var chkDateTo = training.trainingDates.Select(training=>t.DateTo !=null);
var a = chkDateTo.GetEnumerator();
a.MoveNext();
var chkIfExist = a.Current;
var fromRange = training.First().DateFrom.ToString("MMMM dd, yyyy")
var toRange = "";

if(chkIfExist == true){
    toRange = training.First().DateTo.ToString("MMMM dd, yyyy");
}
//chk if dateTo exists
if(fromRange == toRange){
    toRange = null;
}
var trainingRange = (toRange == null ? fromRange:(fromRange + "-"toRange))