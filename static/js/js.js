function findlyrics() {
    $.get("https://api.lyrics.ovh/v1/" + this.document.getElementById("song_artist").value + "/" + this.document.getElementById("song_title").value,
      function (data) {
        var result = document.getElementById("output")
        result.innerHTML = data.lyrics.replace(new RegExp("\n", "g"), "<br>").replace('Paroles de la chanson', ' ').replace('par', 'by').bold();
      })
  }

function showLyrics() {
  let artist = $('#artist').text()
  let title = $('#songTitle').text()
  console.log(artist)
  console.log(title)
  $.get("https://api.lyrics.ovh/v1/" + artist + "/" + title,
  function (data) {
    var result = document.getElementById("output")
    result.innerHTML = data.lyrics.replace(new RegExp("\n", "g"), "<br>").replace('Paroles de la chanson', ' ').replace('par', 'by').bold();
  })
}

  function checkForLyrics() {
    var url = "https://api.lyrics.ovh/v1/" + document.getElementById('song_artist').value + "/" + document.getElementById("song_title").value
    var http = new XMLHttpRequest();
    http.open('HEAD', url, false);
    http.send();
    if (http.status == 404) {
      alert('Please Enter Valid Song/Artist Name');
      window.location.reload();
    }
  }


  $('.lyrics-search').keydown(function (e) {
    if (e.keyCode == 13) {
      e.preventDefault();
      return false;
    }
  });

  const x = document.getElementById('playlist_btn')
  function showButton(x) {
    x.style.visibility = 'visible'
  };