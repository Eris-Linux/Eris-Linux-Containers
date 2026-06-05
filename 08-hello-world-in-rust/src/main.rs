use axum::{Router, response::Html, routing::get};
use std::time::Duration;

async fn std_out_hello() {
    let mut interval = tokio::time::interval(Duration::from_secs(5));

    loop {
        interval.tick().await;
        println!("Hello, World (from Rust)!");
    }
}

#[tokio::main]
async fn main() {
    tokio::spawn(std_out_hello());

    // build our application with a route
    let app = Router::new().route("/", get(handler));

    // run it
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000")
        .await
        .unwrap();
    println!("listening on {}", listener.local_addr().unwrap());
    axum::serve(listener, app).await;
}

async fn handler() -> Html<&'static str> {
    Html("<h1>Hello, World (from Rust)!</h1>")
}
