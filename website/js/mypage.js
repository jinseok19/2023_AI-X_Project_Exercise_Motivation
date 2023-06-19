document.addEventListener("DOMContentLoaded", function () {
  var calendarEl = document.getElementById("calendar");

  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: "dayGridMonth",
    initialDate: "2023-06-16",
    headerToolbar: {
      left: "prev,next today",
      center: "title",
      right: "dayGridMonth,timeGridWeek,timeGridDay",
    },
    events: [

      {
        title: "workout",
        start: "2023-05-12T10:30:00",
        end: "2023-05-12T12:30:00",
      },
      {
        title: "workout",
        start: "2023-05-13T10:30:00",
        end: "2023-05-13T12:30:00",
      },
      {
        title: "workout",
        start: "2023-06-05T10:00:00",
        end: "2023-06-05T13:00:00",
      },
      {
        title: "workout",
        start: "2023-06-07T14:00:00",
        end: "2023-06-07T16:00:00",
      },
      {
        title: "workout",
        start: "2023-06-10T12:00:00",
        end: "2023-06-10T13:00:00",
      },
      {
        title: "workout",
        start: "2023-06-12T10:30:00",
        end: "2023-06-12T14:30:00",
      },
      {
        title: "workout",
        start: "2023-06-14T17:30:00",
        end: "2023-06-14T19:30:00",
      },
      {
        title: "workout",
        start: "2023-06-15T12:30:00",
        end: "2023-06-15T14:30:00",
      },
      {
        title: "workout",
        start: "2023-06-16T12:00:00",
        end: "2023-06-16T13:00:00",
      },

    ],
  });

  calendar.render();
});
