#!/bin/sh

main() {
  CONFIG="${CONFIG:-./config.sh}"

  case $1 in
    -h | --help )
      show_help
      exit
      ;;

    -c | --config )
      CONFIG="$2"
      ;;
  esac

  . "$CONFIG"
  
  mv README-template.md README.md
  mv ntdocutils-theme-NAME "ntdocutils-theme-$NAME"

  replace_values "Name" "$NAME"
  replace_values "Version" "$VERSION"
  replace_values "Description" "$DESCRIPTION"
  replace_values "URL" "$URL"
  replace_values "Author" "$AUTHOR"
  replace_values "Email" "$EMAIL"
  replace_values "Server" "$SERVER"

  rm -rf .git config.sh setup.sh
  git init
}

show_help() {
  cat <<EOF
Usage: $0 [-c CONFIG_FILE | --config CONFIG_FILE]

-c CONFIG_FILE, --config CONFIG_FILE
  Uses a custom configuration file. (./config.sh)

-h, --help
  Shows this help text.
EOF
}

replace_values() {
  key="$1"
  value="$2"
  target="${3:-.}"

  escaped=$(
    echo "$value" |
    sed -re "s/\/+/\\\\\//g" |
    sed -re "s/(\\\\)?\/$//g"
  )

  for file in $(grep -lr "$key" "$target"); do
    sed -re "s/\{\{ $key \}\}/$escaped/g" -i "$file"
  done
}

main $@

