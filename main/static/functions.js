document.addEventListener('DOMContentLoaded', function () {
    function updateBackgroundImages() {
        const wallPaper = document.getElementById('baseWallpaper');
        const originalUrl = wallPaper.getAttribute('data-small');
        const croppedUrl = wallPaper.getAttribute('data-large');

        // Check window size and update image file name
        if (window.innerWidth <= 991) {
            wallPaper.src = originalUrl;  // Use the small image for smaller screens
        } else {
            wallPaper.src = croppedUrl;   // Use the large image for larger screens
        }

        // Log the updated image source (for debugging purposes)
        console.log(wallPaper.src);
    }

    // Call the function on initial load
    updateBackgroundImages();

    // Update the image on window resize
    window.addEventListener('resize', updateBackgroundImages);
});
