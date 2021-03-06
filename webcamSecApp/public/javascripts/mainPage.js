(function(){
  const mouseJail = document.getElementById('mouseJail'),
    video = document.getElementById('video'),
    canvas = document.getElementById("canvas"),
    vendorUrl = window.URL;

  let context = canvas.getContext('2d');

    navigator.getMedia =  navigator.getUserMedia ||
                          navigator.webkitGetUserMedia ||
                          navigator.mozGetUserMedia ||
                          navigator.msGetUserMedia;

  navigator.getMedia({
    video: true,
    audio: false,
  }, function(stream){
    video.srcObject=stream;;
    video.play()
  }, function(error){
    console.error(error); 
  });
  mouseJail.addEventListener('mouseleave', function(){
    var currentdate = new Date();
    console.log(`${currentdate.getMonth() + 1}/${currentdate.getDate()}/${currentdate.getFullYear()} @ 
 ${currentdate.getHours()}:${currentdate.getMinutes()}`);
    context.drawImage(video, 0, 0, 400, 300)
});
})()