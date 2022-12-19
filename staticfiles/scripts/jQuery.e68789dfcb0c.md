THE BASIC TO USE JQUERY



1. INSTALLATION
    Can be downloaded here: https://jquery.com/download/
    and to use the downloaded file you only need to sorce it wherever
    html file you are working with in a head section.

    <head>
        <script src="jquery.js"></script>
    </head>


2.  SYNTAX
    Jquery syntax is basically simple, it follows this structure
    $(selector).action()
    where:
    $   -> calls the jquery library
    (selector)  -> find or select the html element
    action()    -> is the action to be takken

    Example:
    To hide all paragraphs on button click
    $(document).ready(function() {
        $('button').click(function() {
            $('p').hide([optional time in milisecs])
        })
    })


3.  SELECTORS
    a)  Selecting form inputs or position
            $(':type').action() // input
            $('p:first').action() // first paragraphs

    b)  Selecting by class, id or attribute
            $('.class').action()
            $('#id').action()
            $('[attr]').action()
    
    c)  Selecting by tagname
            $('tagname').action()
    
    d)  Selecting all 
            $('*').action() // selects the DOM


3. EVENTS
    Jquery supports all html events and they can be used as 
    follow:
    a) to attach a single event to a selector
    $(selector).event(callback function)

    b)to attach one or multiple events to a selector
    $(selector).on(
        'event', callback
    )

    $(selector).on(
        {event: callback},
        {event2: callback},
        {eventN: callback}
    )


4.  EFFETCTS
    With Jquery you an manipulate effects on in a DOM.
    Here are some available effects you can work with:
    hide()      =   hides all selected html elements
    show()      =   its hide opposite method
    toggle()    =   attach the toggle effect (e.g. show and hide)
    fadeIn()    =   attach the fade in effect
    fadeIn()    =   attach the fade out effect
    fadeToggle()    =   combination of the fadeIn() and fadeOut() effect
    fadeTo()    =   manipulates the html opacity
    slideDown()     =   to slide down
    sideUp()    =   to slide up
    sideToggle()    =   toogle slide


5. ANIMATIONS

    .animate('animation-name')
    .animate({
        key: value,
        key2: value2,
    })
