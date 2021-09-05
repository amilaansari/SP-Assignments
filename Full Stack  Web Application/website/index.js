window.addEventListener("DOMContentLoaded", function() {
    //1: Display menu results on load
    fetch ("http://localhost:5000/menu", {method: "GET"})

    //convert server response into JSON
    .then(function (response) {
        return response.json();
    })
    //retrieve desired data from JSON body and display
    .then (function(json) {
        getData(json);
    });

    //2: Sort menu results when sort button is clicked, i.e WITHOUT searchInput
    //track clickCount
    var clickCount = 0;
    $("#nav_sort_btn").on("click", function() {
        //add 1 for every click
        clickCount ++;

        //2a: Sort menu by price DESC
        if ( clickCount%2 == 0 ){
            fetch ("http://localhost:5000/menu/desc", {method: "GET"})

            //convert server response into JSON format
            .then(function (response) {
                return response.json();
            })
            //retrieve and display desired data from JSON response
            .then (function(json) {
                getData(json);
            });
        }
        //2b: Sort menu by price ASC
        else {
            fetch ("http://localhost:5000/menu/asc", {method: "GET"})

            //convert server response into JSON format
            .then(function (response) {
                return response.json();
            })
            //retrieve and display desired data from JSON response
            .then (function(json) {
                getData(json);
            });
        }
    })

    //3: Return menu search results when search button is clicked
    document.getElementById("nav_search_btn").addEventListener("click", function() {
        //retrieve user's search input
        const searchInput = document.getElementById("nav_search_text").value;

        //send HTTP request to server with user's search input
        fetch ("http://localhost:5000/menu/search/" + searchInput, {method: "GET"})

        //convert server response into JSON format
        .then(function (response) {
            return response.json();
        })
        //retrieve desired data from JSON response
        .then (function(json) {
            getData(json);
        });
        
        //4: Sort menu search results when sort button is clicked, i.e WITH searchInput
        //unsolved bug: two displays are triggered (2: and 4:) because events are triggered by same click function
        //track clickCt
        var clickCt = 0;
        $("#nav_sort_btn").on("click", function() {
            //add 1 for every click
            clickCt ++;

            //4a: Sort menu based on searchInput, by price DESC
            if ( clickCt%2 == 0 ){
                //send HTTP request to server with user's search input
                fetch ("http://localhost:5000/menu/search/desc/" + searchInput, {method: "GET"})

                //convert server response into JSON format
                .then(function (response) {
                    return response.json();
                })
                //retrieve and display desired data from JSON response
                .then (function(json) {
                    getData(json);
                });
            }

            //4b: Sort menu based on searchInput, by price ASC
            else {
                //send HTTP request to server with user's search input
                fetch ("http://localhost:5000/menu/search/asc/" + searchInput, {method: "GET"})

                //convert server response into JSON format
                .then(function (response) {
                    return response.json();
                })
                //retrieve and display desired data from JSON response
                .then (function(json) {
                    getData(json);
                });
            }
        })

    });

    //5: Format data from JSON for display as a table
    function getData(json) {
        //create menuResults array
        const searchResults = []
        //allow for multiple results
        for (i = 0; i < json.menuItems.length; i++) {
            //table row for each search result, table cell for each search result's value,
            searchResult = "<tr> <td>" + json.menuItems[i].name + "</td> <td>" + json.menuItems[i].price + "</td> <td>" + json.menuItems[i].stall_name + "</td> </tr>";
            //append each result into searchResults array
            searchResults.push(searchResult);      
        }  
        //change array into string to allow removal of ','
        menuString = searchResults.join()
        menuString = menuString.replace(/\,/g,"")
        //display resulting string as a table
        document.getElementById("table_body").innerHTML= menuString;
    }
});
