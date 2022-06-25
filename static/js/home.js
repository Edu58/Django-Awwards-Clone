$('.details').hide()
$('.card').on('mouseover', function () {
    $(this).children('.project-image').addClass('blur')
    $(this).children('.details').fadeIn("fast")
})
$('.card').on('mouseleave', function () {
    $(this).children('.project-image').removeClass('blur')
    $(this).children('.details').fadeOut("fast")
})