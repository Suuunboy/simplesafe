const audioPlayer = document.getElementById('audioPlayer');
    const playlist = document.querySelectorAll('.track');

    playlist.forEach(track => {
        track.addEventListener('click', function() {
            audioPlayer.src = this.getAttribute('data-src');
            audioPlayer.play();
        });
    });