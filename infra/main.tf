resource "helm_release" "nginx_ingress" {
  name             = "ingress-nginx"
  repository       = "https://kubernetes.github.io/ingress-nginx"
  chart            = "ingress-nginx"
  namespace        = "ingress-nginx"
  create_namespace = true
  values = [<<EOF
controller:
  service:
    annotations:
      networking.gke.io/load-balancer-type: "External"
EOF
  ]
  depends_on = [google_container_cluster.my_cluster]
}
