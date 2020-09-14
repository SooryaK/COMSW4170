//author: Soorya Kumar
//COMS4170
//HW7

//////////////////////////////////////////////////////
//Model fucntions
//////////////////////////////////////////////////////

function search_podcasts(podcast_search) {
    $.ajax({
        type: "POST",
        url: "fetch_podcasts",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(podcast_search),
        success: function (result) {
            var all_data = result["podcasts"]
            podcasts = all_data
            display_podcasts_list(podcasts, false, podcast_search["search_name"])
        },
        error: function (request, status, error) {
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function getPodcastDetails(podcastId) {
    $.ajax({
        type: "GET",
        url: "view/" + podcastId,
        dataType: "json",
        success: function (result) {
            podcast_details = result["chosen_podcast"]
            display_podcast_details()
        },
        error: function (request, status, error) {
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function deletePodcast(id) {
    $.ajax({
        type: "POST",
        url: "delete_podcast",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify({ "id": id }),
        success: function (result) {
            podcastID = result["podcastID"]
            var rowID = "#row" + podcastID
            $(rowID).remove();
        },
        error: function (request, status, error) {
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function addNewPodcast(new_podcast) {
    $.ajax({
        type: "POST",
        url: "add_podcast",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(new_podcast),
        success: function (result) {
            podcast_titles = result["podcast_titles"]
            podcast_details = result["podcast_details"]
            create_page = [{ "create_page": "yes" }]
            //display_podcast_details()
            display_create_page(true);
        },
        error: function (request, status, error) {
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function update_podcast(field, update, id) {
    var update_json = {}
    if (field == "description") {
        update_json["Description"] = update;
        update_json["ID"] = id;
    }
    else if (field == "website") {
        update_json["Website"] = update;
        update_json["ID"] = id;
    }
    $.ajax({
        type: "POST",
        url: "update_podcast",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(update_json),
        success: function (result) {
            podcast_details = result["chosen_podcast"]
            create_page = [{ "create_page": "no" }]
            display_podcast_details()
        },
        error: function (request, status, error) {
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function update_category(updated_category, marked_as_deleted, id) {
    category = {
        "Category": updated_category,
        "marked_as_deleted": marked_as_deleted,
        "ID": id
    }
    $.ajax({
        type: "POST",
        url: "update_category",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(category),
        success: function (result) {
            podcast_details = result["chosen_podcast"]
            create_page = [{ "create_page": "no" }]
            display_podcast_details()
        },
        error: function (request, status, error) {
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

//////////////////////////////////////////////////////
//View functions
//////////////////////////////////////////////////////


//this function updates the UI with the lists of podcasts the user has searched for
function display_podcasts_list(podcasts, home, search_name) {
    if (create_page != null && create_page[0]["create_page"] == "yes") {
        display_create_page();
        return;
    }

    //set up the updated html
    var updatedPodcastsList = '<h4 id="mission">Helping Commuters and other Podcast Listeners find their next listen!</h4>';
    if (home == undefined || home == false) {
        updatedPodcastsList += '<h4 id="results">' + podcasts.length.toString() + ' Results</h4>';
    }
    updatedPodcastsList += '<br /><br />';
    if (podcasts != null) {
        for (i = 0; i < podcasts.length; i++) {
            if (i % 4 == 0) {
                updatedPodcastsList +=
                    '<div class = "row toprowpadding">';
            }
            var title = podcasts[i].Title.toString()
            if (search_name != undefined) {
                var re = new RegExp(search_name, 'gi')
                var to_replace = title.match(re)[0];
                var replacement = '<mark class="bold">' + title.match(re)[0] + '</mark>';
                title = title.replace(to_replace, replacement);
                // if (title.match(re)) {
                //     var a = title.match(re).length;
                //     for (j = 0; j < title.match(re).length; j++) {
                //         var to_replace = title.match(re)[j];
                //         var replacement = '<mark class="bold">' + title.match(re)[j] +'</mark>';
                //         title = title.replace(to_replace, replacement);
                // }
            }
            updatedPodcastsList +=
                '<div class = "card podcastcard col-md-3 col-sm-6" id = "card' + podcasts[i].ID.toString() + '" > \
                                <img src="' + podcasts[i].Image.toString() + '" class="card-img-top img-fluid podcastcardimage" alt="Podcast Cover Art for '+ podcasts[i].Title.toString() +'">\
                                <div class="card-body"> \
                                    <h5 class="card-title"> '+ title + ' </h5>\
                                    <h6 class="card-subtitle mb-2 text-muted">'+ podcasts[i].Author.toString() + ' </h6>\
                                    <p class="card-text"> Overall Rating: '+ podcasts[i].Rating.toString() + ' <\p>\
                                </div> \
                            </div>';
            if (i % 4 == 3 || i == podcasts.length - 1) {
                updatedPodcastsList +=
                    '</div>';
            }
        }
    }
    else {
        updatedPodcastsList +=
            '<div class = "row toprowpadding"> \
                <div class="col-md-3 bold"> No Results Found </div> \
            </div>';
    }

    console.log(updatedPodcastsList);
    //update the html
    $("#mainbody").html(updatedPodcastsList);
    //rebind all event handlers
    eventHandlerBindings("list");
    $("#podcast_title_textbox").val("");
    $("#podcast_title_textbox").focus();
}

//this function updates the UI with the podcast details for the podcast the user has clicked on
function display_podcast_details() {
    var chosen_podcast_details = podcast_details;
    var updatedPodcastsList = "";
    if (podcast_details != null) {
        var categories = "";
        for (i = 0; i < chosen_podcast_details[0].Category.length; i++) {
            if (!chosen_podcast_details[0].Category[i]["marked_as_deleted"]) {
                categories += '<span id="category' + i + '">'
                categories += chosen_podcast_details[0].Category[i]["Name"]
                categories += '&nbsp;<button id="btnDeleteCategory' + i + '" class="btn btn-mini btnedit btnDeleteCategory" data-span="category'+ i +'" data-catname="' + chosen_podcast_details[0].Category[i]["Name"] + '">Delete</button><br />'
                categories += '</span>'
            }
            else {
                categories += '<span id="category' + i + '">'
                categories += '&nbsp;<button id="btnUndoCatDelete' + i + '" class="btn btn-mini btnedit btnUndoCatDelete" data-span="category'+ i +'" data-catname="' + chosen_podcast_details[0].Category[i]["Name"] + '">Undo Delete</button><br />'
                categories += '</span>'                
            }
        }
        updatedPodcastsList +=
            '<div class = "row toprowpadding"> \
                <div class="col-md-6"> \
                    <h4 id="view_title" data-id="'+ chosen_podcast_details[0].ID.toString() + '" class="bold">' + chosen_podcast_details[0].Title.toString() + ' </h4>\
                    <span class="bold">Created by:</span> '+ chosen_podcast_details[0].Author.toString() + '\
                    <br \><br \><br \>\
                    <span class="bold">Description:</span> \
                    <span id="view_description"> \
                    '+ chosen_podcast_details[0].Description.toString() + '&nbsp;<button id="btnEditDescPodcast" class="btn btn-mini btnedit">Edit Description</button>\
                    </span>\
                    <br \>\
                    <span id="view_description_buttons"> \
                    </span>\
                    <span class="bold">Website:</span> \
                    <span id="view_website"> \
                    <a href="'+ chosen_podcast_details[0].Website.toString() + '">' + chosen_podcast_details[0].Website.toString() + '</a>&nbsp;<button id="btnEditWebsitePodcast" class="btn btn-mini btnedit">Edit Website</button>\
                    </span>\
                    <br \>\
                    <span id="view_website_buttons"> \
                    </span>\
                    <span class="bold">Overall Rating:</span> '+ chosen_podcast_details[0].Rating.toString() + '\
                    <br \><br \><br \>\
                    <span class="bold">Language:</span> '+ chosen_podcast_details[0].Language.toString() + '\
                    <br \>\
                    <span class="bold">Categories:</span><br />'+ categories + '\
                </div> \
                <div class="col-md-4"> \
                    <img src="'+ chosen_podcast_details[0].Image.toString() + '" class="img-fluid" alt="Podcast Cover Art for '+ chosen_podcast_details[0].Title.toString() +'">\
                </div> \
            </div>';
    }
    else {
        updatedPodcastsList +=
            '<div class = "row toprowpadding"> \
            <div class="col-md-3 bold"> No Results Found </div> \
        </div>';
    }
    console.log(updatedPodcastsList);
    //update the html
    $("#mainbody").html(updatedPodcastsList);
    //rebind all event handlers
    eventHandlerBindings("details");
    $("#podcast_title_textbox").val("");
    $("#podcast_title_textbox").focus();
}

//this function updates the UI with the the create page
function display_create_page(create_success) {
    var chosen_podcast_details = podcast_details;
    var podcastsCreate = "";
    podcastsCreate +=
        '<div class = "row toprowpadding"> \
            <div class="col-md-8"> \
                <div class="row createrowpadding"> \
                    <div class="col-md-3"> \
                        <span class="bold">Title: </span>\
                    </div> \
                    <div class="col-md-9"> \
                        <input type="text" class="new_podcast_textbox" id="new_podcast_title_textbox" placeholder="ex. Amazing Podcast You Should Listen To">\
                        <span class="warning" id="warning_title"></span>\
                    </div> \
                </div> \
                <div class="row createrowpadding"> \
                    <div class="col-md-3"> \
                        <span class="bold">Created By: </span>\
                    </div> \
                    <div class="col-md-9"> \
                        <input type="text" class="new_podcast_textbox" id="new_podcast_author_textbox" placeholder="ex. Amazing Person Or Company">\
                        <span class="warning" id="warning_author"></span>\
                    </div> \
                </div> \
                <div class="row createrowpadding"> \
                    <div class="col-md-3"> \
                        <span class="bold">Image URL: </span>\
                    </div> \
                    <div class="col-md-9"> \
                        <input type="text" class="new_podcast_textbox" id="new_podcast_image_textbox" placeholder="ex. http://is1.mzstatic.com/image/source/600x600bb.jpg">\
                        <span class="warning" id="warning_image"></span>\
                    </div> \
                </div> \
                <div class="row createrowpadding"> \
                    <div class="col-md-3"> \
                        <span class="bold">Website: </span>\
                    </div> \
                    <div class="col-md-9"> \
                        <input type="text" class="new_podcast_textbox" id="new_podcast_webiste_textbox" placeholder="ex. https://www.amazingpodcast.com">\
                        <span class="warning" id="warning_website"></span>\
                    </div> \
                </div> \
                <div class="row createrowpadding"> \
                    <div class="col-md-3"> \
                        <span class="bold">Description: </span>\
                    </div> \
                    <div class="col-md-9"> \
                        <textarea type="text" class="new_podcast_textbox" id="new_podcast_description_textbox" rows="4" placeholder="ex. Amazing Person Or Company Talks about Super Interesting Topic"></textarea>\
                        <span class="warning" id="warning_description"></span>\
                    </div> \
                </div> \
                <div class="row createrowpadding"> \
                    <div class="col-md-3"> \
                        <span class="bold">Overall Rating: </span>\
                    </div> \
                    <div class="col-md-9"> \
                        <input type="text" class="new_podcast_textbox" id="new_podcast_rating_textbox" placeholder="ex. 4.8">\
                        <span class="warning" id="warning_rating"></span>\
                    </div> \
                </div> \
                <div class="row createrowpadding"> \
                    <div class="col-md-3"> \
                        <span class="bold">Languange: </span>\
                    </div> \
                    <div class="col-md-9"> \
                        <input type="text" class="new_podcast_textbox" id="new_podcast_language_textbox" placeholder="ex. English">\
                        <span class="warning" id="warning_language"></span>\
                    </div> \
                </div> \
                <div class="row createrowpadding"> \
                    <div class="col-md-3"> \
                        <span class="bold">Categories: </span>\
                    </div> \
                    <div class="col-md-9"> \
                        <input type="text" class="new_podcast_textbox" id="new_podcast_categories_textbox" placeholder="Seperate with Commas ex. Gadgets, Technology, Tech News">\
                        <span class="warning" id="warning_category"></span>\
                    </div> \
                </div> \
            </div> \
            <div class="col-md-4"> \
                <button id="btnAddPodcast" class="btn btn-primary">Add Podcast</button> \
            </div> \
        </div>';

    console.log(podcastsCreate);
    //update the html

    //rebind all event handlers
    if (create_success != undefined && create_success) {
        var create_success_html = '<div id="create_success" class="row"> \
                                        <div class = "row"> \
                                            <div class="col-md-8"> \
                                                <div class="row createrowpadding"> \
                                                    <div class="col-md-3"> \
                                                    </div> \
                                                    <div class="col-md-9" id="create_success_text"> \
                                                    New Item Successfully Created \
                                                    </div> \
                                                </div> \
                                            </div> \
                                            <div class="col-md-4" id="create_success_button"> \
                                                <button class="btn btn-primary" id="btnCreatedView">View Created Podcast</button>\
                                            </div> \
                                        </div> \
                                    </div>';
        podcastsCreate = create_success_html + podcastsCreate;
    }
    $("#mainbody").html(podcastsCreate);
    eventHandlerBindings("create");
    $("#podcast_title_textbox").val("");
    $("#new_podcast_title_textbox").focus();
}

//this function dynamically adds/re-adds the event handler bindings for all our elements every time the UI is updated (it is called in updateUI)
function eventHandlerBindings(page_type) {
    //binds autocomplete handler to input textbox with id of podcast_title_textbox, source specifices the data autocomplete works with 
    $("#podcast_title_textbox").autocomplete({
        source: podcast_titles,
        minLength: 1
    })
    //binds click handler to input textbox with id of podcast_title_textbox, and triggers search event as soon as input box is clicked
    //if minLength property is set to 0 for autocomplete then all options are displayed when input box is clicked
    $("#podcast_title_textbox").click(function () {
        $("#podcast_title_textbox").autocomplete("search", "minLength: 1");
    })
    //binds keypress event to reams input box, checks to see if Enter key was the key pressed and only performs action if it was
    $("#podcast_title_textbox").keypress(function (event) {
        var keycode = (event.keyCode ? event.keyCode : event.which);
        if (keycode == '13') {
            podcast_search_name = $("#podcast_title_textbox").val();
            var podcast_search = {
                "search_name": podcast_search_name,
            }
            search_podcasts(podcast_search)
        }
    })
    //binds click event to the Submit button
    $("#btnSubmit").click(function () {
        podcast_search_name = $("#podcast_title_textbox").val();
        var podcast_search = {
            "search_name": podcast_search_name,
        }
        search_podcasts(podcast_search)
    })
    if (page_type == "list") {
        $(".podcastcard").click(function (e) {
            var target = $(e.target)
            //get the id of the delete button clicked
            var id = $(this).attr('id');
            //get the id on the id of the btnDelete 
            var podcastIndex = id.replace("card", "");
            getPodcastDetails(podcastIndex);
        })
        $(".podcastcard").hover(
            function () {
                $(this).addClass("podcastlisthover");
            },
            function () {
                $(this).removeClass("podcastlisthover");
            }
        )
    }
    else if (page_type == "create") {
        $("#btnAddPodcast").click(function () {
            podcast_title = $("#new_podcast_title_textbox").val();
            podcast_author = $("#new_podcast_author_textbox").val();
            podcast_image = $("#new_podcast_image_textbox").val();
            podcast_website = $("#new_podcast_webiste_textbox").val();
            podcast_description = $("#new_podcast_description_textbox").val();
            podcast_rating = $("#new_podcast_rating_textbox").val();
            podcast_language = $("#new_podcast_language_textbox").val();
            podcast_categories = $("#new_podcast_categories_textbox").val();

            var new_podcast = {
                "Title": podcast_title,
                "Author": podcast_author,
                "Image": podcast_image,
                "Website": podcast_website,
                "Description": podcast_description,
                "Rating": podcast_rating,
                "Language": podcast_language,
                "Category": podcast_categories
            };

            var warnings = validateCreate(new_podcast);
            if (warnings.length > 0) {
                setWarnings(new_podcast, warnings)
            }
            else {
                addNewPodcast(new_podcast);
            }
        })
        if ($('#btnCreatedView').length) {
            $("#btnCreatedView").click(function () {
                display_podcast_details();
            })
        }
    }
    else if (page_type == "details") {
        $("#btnEditDescPodcast").click(function () {
            var podcast_description = $("#view_description").text();
            podcast_description = podcast_description.replace("Edit Description", "");
            var updated_buttons = '<button id="btnSubmitDescChange" class="btn btn-mini">Submit</button>&nbsp;<button id="btnDiscardDescChanges" class="btn btn-mini">Discard Changes</button><br />';
            var updated_description_input = '<br /><textarea type="text" class="new_podcast_textbox" id="new_podcast_description_textbox" rows="4" placeholder="ex. Amazing Person Or Company Talks about Super Interesting Topic">' + podcast_description.trim() + '</textarea>';
            $("#view_description").html(updated_description_input);
            $("#view_description_buttons").html(updated_buttons);
            $("#btnEditWebsitePodcast").hide();
            $("#new_podcast_description_textbox").focus();
            $("#btnSubmitDescChange").click(function () {
                var id = $("#view_title").attr("data-id");
                var test = $("#new_podcast_description_textbox").val();
                update_podcast("description", $("#new_podcast_description_textbox").val(), id);
            });
            $("#btnDiscardDescChanges").click(function () {
                var id = $("#view_title").attr("data-id");
                getPodcastDetails(id)
            });
        })
        $("#btnEditWebsitePodcast").click(function () {
            var podcast_website = $("#view_website").text();
            podcast_website = podcast_website.replace("Edit Website", "");
            var updated_buttons = '<button id="btnSubmitWebsiteChange" class="btn btn-mini">Submit</button>&nbsp;<button id="btnDiscardWebsiteChanges" class="btn btn-mini">Discard Changes</button><br />';
            var updated_website_input = '<br /><textarea type="text" class="new_podcast_textbox" id="new_podcast_webiste_textbox" rows="2" placeholder="ex. https://www.amazingpodcast.com">' + podcast_website.trim() + '</textarea>';
            $("#view_website").html(updated_website_input);
            $("#view_website_buttons").html(updated_buttons);
            $("#btnEditDescPodcast").hide();
            $("#new_podcast_webiste_textbox").focus();
            $("#btnSubmitWebsiteChange").click(function () {
                var id = $("#view_title").attr("data-id");
                update_podcast("website", $("#new_podcast_webiste_textbox").val(), id);
            });
            $("#btnDiscardWebsiteChanges").click(function () {
                var id = $("#view_title").attr("data-id");
                getPodcastDetails(id)
            });
        })
        if ($('.btnDeleteCategory').length) {
            $('.btnDeleteCategory').click(function (event) {
                var id = $("#view_title").attr("data-id");
                var category_name = event.target.dataset.catname;
                update_category(category_name, true, id);
            })
        }
        if ($('.btnUndoCatDelete').length) {
            $('.btnUndoCatDelete').click(function (event) {
                var id = $("#view_title").attr("data-id");
                var category_name = event.target.dataset.catname;
                update_category(category_name, false, id);
            })
        }
    }
}

function validateCreate(new_podcast) {
    var warnings = []
    if (new_podcast["Title"] == "") { warnings.push("TitleBlank"); }
    else { $("#warning_title").html(""); }
    if (new_podcast["Author"] == "") { warnings.push("AuthorBlank"); }
    else { $("#warning_author").html(""); }
    if (new_podcast["Image"] == "") { warnings.push("ImageBlank"); }
    else { $("#warning_image").html(""); }
    if (new_podcast["Website"] == "") { warnings.push("WebsiteBlank"); }
    else { $("#warning_website").html(""); }
    if (new_podcast["Description"] == "") { warnings.push("DescriptionBlank"); }
    else { $("#warning_description").html(""); }
    if (new_podcast["Rating"] == "") { warnings.push("RatingBlank"); }
    else if (isNaN(new_podcast["Rating"])) { warnings.push("RatingNaN"); }
    else if (parseFloat(new_podcast["Rating"]) < 0 || parseFloat(new_podcast["Rating"]) > 5) { warnings.push("RatingOfR"); }
    else $("#warning_rating").html("");
    if (new_podcast["Language"] == "") { warnings.push("LanguageBlank"); }
    else $("#warning_language").html("");
    if (new_podcast["Category"] == "") { warnings.push("CategoryBlank"); }
    else $("#warning_category").html("");
    return warnings;
}

function setWarnings(new_podcast, warnings) {
    if (warnings.includes("TitleBlank")) { $("#warning_title").html("Title cannot be blank!"); }
    if (warnings.includes("AuthorBlank")) { $("#warning_author").html("Author cannot be blank!"); }
    if (warnings.includes("ImageBlank")) { $("#warning_image").html("Image cannot be blank!"); }
    if (warnings.includes("WebsiteBlank")) { $("#warning_website").html("Website cannot be blank!"); }
    if (warnings.includes("DescriptionBlank")) { $("#warning_description").html("Description cannot be blank!"); }
    if (warnings.includes("RatingBlank")) { $("#warning_rating").html("Rating cannot be blank!"); }
    if (warnings.includes("RatingNaN")) {
        $("#warning_rating").html("Rating must be a Number!");
        $("#new_podcast_rating_textbox").val(new_podcast["Rating"]);
    }
    if (warnings.includes("RatingOfR")) {
        $("#warning_rating").html("Rating must be between 0 and 5!");
        $("#new_podcast_rating_textbox").val(new_podcast["Rating"]);
    }
    if (warnings.includes("LanguageBlank")) { $("#warning_language").html("Language cannot be blank!"); }
    if (warnings.includes("CategoryBlank")) { $("#warning_category").html("Category cannot be blank!"); }
}

$(document).ready(function () {
    display_podcasts_list(podcasts, true);
})