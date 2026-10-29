use crawlora_opendota::{serde_json, Client, OpendotaHeroesParams};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client.opendota.heroes(Default::default()).await?;
    let data: serde_json::Value = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
