export default async function handler(req, res) {
const key = process.env.ANTHROPIC_KEY;
res.status(200).json({keyExists: !!key, keyLength: key ? key.length : 0});
}
