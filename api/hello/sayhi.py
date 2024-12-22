def handler(req, res):
  # Your python script logic goes here
  print("hello from cron")
  res.status(200).send("Cront job execute cute cute")
