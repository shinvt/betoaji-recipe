// -----------------Like Button----------------------
var btnClassClick = function(e){
    var recipeID = e.currentTarget.id.split("_")[1];
    $.ajax({
        url: '/recipes/'+recipeID+'/like/',
        dataType: 'json',
        success: function (data) {
          var like_status = data;
    			if (like_status.Success == "True") {
      			$(e.currentTarget).css("color", "red");
      			$('#like-count' + '_' + recipeID).text(like_status.count);
    			} else if (like_status.Removed == "True") {
            $(e.currentTarget).css("color", "black");
      			$('#like-count' + '_' + recipeID).text(like_status.count);
          }
        },
        error: function(data) {
         	console.log("AJAX's like error")
        }/*  end of error */
    });
}

$('.like-icon').on('click', btnClassClick);

// -----------------Donation----------------------
// Create a Stripe client.
var stripe = Stripe('pk_test_7jQjbysQY8LT2ObxAOTiI40B001vsRQY7P');

// Create an instance of Elements.
var elements = stripe.elements();

// Custom styling can be passed to options when creating an Element.
// (Note that this demo uses a wider set of styles than the guide below.)
var style = {
  base: {
    color: '#32325d',
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4'
    }
  },
  invalid: {
    color: '#fa755a',
    iconColor: '#fa755a'
  }
};

// Create an instance of the card Element.
var card = elements.create('card', {style: style});

// Add an instance of the card Element into the `card-element` <div>.
card.mount('#card-element');

// Handle real-time validation errors from the card Element.
card.addEventListener('change', function(event) {
  var displayError = document.getElementById('card-errors');
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = '';
  }
});

// Handle form submission.
var form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
  event.preventDefault();

  stripe.createToken(card).then(function(result) {
    if (result.error) {
      // Inform the user if there was an error.
      var errorElement = document.getElementById('card-errors');
      errorElement.textContent = result.error.message;
    } else {
      // Send the token to your server.
      stripeTokenHandler(result.token);
    }
  });
});

// Submit the form with the token ID.
function stripeTokenHandler(token) {
  // Insert the token ID into the form so it gets submitted to the server
  var form = document.getElementById('payment-form');
  var hiddenInput = document.createElement('input');
  hiddenInput.setAttribute('type', 'hidden');
  hiddenInput.setAttribute('name', 'stripeToken');
  hiddenInput.setAttribute('value', token.id);
  form.appendChild(hiddenInput);

  // Submit the form
  form.submit();
}

// -----------------Donation Chart----------------------
var $donationChart = $("#donation-chart");
      $.ajax({
        url: $donationChart.data("url"),
        success: function (data) {

          var ctx = $donationChart[0].getContext("2d");

          console.log(data.years)

          new Chart(ctx, {
            type: 'bar',
            data: {
              labels: data.years,
              datasets: [{
                label: 'Donated Amount Per Year',
                data: data.donate_amount,
                backgroundColor: "rgba(255,0,0,0.4)",
                borderColor: "red",
              }]
            },
            options: {
              responsive: true,
              scales: {
                  xAxes: [{
                    scaleLabel: {
                            display: true,
                            labelString: 'Year',
                            fontColor: "red",
                            fontSize: 16
                        },
                    gridLines: {
                        color: "rgba(255, 0, 0, 0.2)",
                    },
                    ticks: {
                        fontColor: "red",
                        fontSize: 14
                    }
                  }],
                  yAxes: [{
                      ticks: {
                          beginAtZero: true
                      }
                  }]
              },
              legend: {
                position: 'top',
              },
              title: {
                display: true,
                text: 'Donation Chart'
              }
            }
          });

        }
    });
