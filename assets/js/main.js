import $ from "jquery";

global.jQuery = global.$ = $;

(($) => {
  $(() => {
    $(document).on("click", "#ad22", () => {
      console.log("OK!");
    });
  });
})($);
