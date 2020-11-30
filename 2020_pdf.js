function download_file(fileURL, fileName) {
  var link = document.createElement('a');
  link.href = fileURL;
  link.download = fileName;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
var i
for(i=1; i<=3; i++)
{
var fileURL = "http://138.25.65.123/in/cases/cen/INSC/2020/"+i+".pdf";
var fileName = i+".pdf";
console.log(fileURL)
download_file(fileURL, fileName);
}