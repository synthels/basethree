import YAML from "yaml";
import axios from "axios";

axios.defaults.withCredentials = true;

async function getConf() {
  const r = await axios({
    url: "config.yml",
    method: "get",
  });

  return YAML.parse(r.data);
}

export async function post(url: string, params: Object) {
  const conf = await getConf();
  return axios.post(new URL(url, conf.api).toString(), params);
}

export async function get(url: string, params: Object) {
  const conf = await getConf();
  return axios.get(new URL(url, conf.api).toString(), params);
}
