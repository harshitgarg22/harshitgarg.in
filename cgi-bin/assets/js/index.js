function show(el) {
  el.classList.add("show");
  el.classList.remove("hide");
}

function hide(el) {
  el.classList.add("hide");
  el.classList.remove("show");
}

window.displayGreetings = function displayGreetings(greetings) {
  // greetings is retrieved from backend through jinja in index.html

  let divGreeting = document.getElementById("greetings");
  // let headerGreeting = document.getElementById("greetings-header");
  let commandSuffixGreeting = document.getElementById(
    "greetings-command-suffix"
  );
  let commandPrefixGreeting = document.getElementById(
    "greetings-command-prefix"
  );
  let commandDisplayGreeting = document.getElementById(
    "greetings-command-display"
  );
  let languageGreeting = document.getElementById("greetings-language");

  commandDisplayGreeting.innerText = greetings.display_text;

  const fx = new TextScramble(commandPrefixGreeting);

  counter = 0;
  const next = () => {
    commandSuffixGreeting.innerText = greetings.commands_suffix[counter];
    fx.setText(greetings.commands_prefix[counter]).then(() => {
      setTimeout(next, 1800);
      this.hide(languageGreeting);
      // this.hide(headerGreeting);
    });
    this.hide(languageGreeting);
    this.show(languageGreeting);
    languageGreeting.innerText = greetings.languages[counter];
    // let header = greetings.headers[counter];
    // if (header != "") {
    // this.hide(headerGreeting);
    // headerGreeting.innerText = greetings.headers[counter];
    // this.show(headerGreeting);
    // }
    counter = (counter + 1) % greetings.languages.length;
  };

  next();
};
