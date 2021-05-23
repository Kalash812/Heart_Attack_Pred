makedir -p ~/.Heart_app/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.Heart_app.toml