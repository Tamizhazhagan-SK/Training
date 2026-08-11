# Rook & Ceph: Cloud-Native Storage Learning Notes

---

## 1. Introduction to Rook and Ceph
* **Rook:** An open-source **cloud-native storage orchestrator** (implemented as a Kubernetes Operator). It automates storage management tasks—such as provisioning, scaling, upgrading, and monitoring—and integrates storage systems natively into Kubernetes.
* **Ceph:** A highly scalable, open-source **distributed storage system** that provides object storage, block storage, and file storage simultaneously (unified storage).

---

## 2. How Rook Works with Kubernetes
* **The Rook Operator:** A specialized Kubernetes Operator that continuously watches for custom resource definitions (CRDs) and manages the entire lifecycle of the underlying storage backend.
* **Declarative Management (CRDs):** Rook introduces custom Kubernetes objects (like `CephCluster`, `CephBlockPool`, and `CephObjectStore`) allowing you to configure and manage your storage infrastructure using standard `kubectl` commands and YAML manifests.

---

## 3. Core Ceph Components in a Kubernetes Cluster
When Rook provisions Ceph, it runs several internal daemons as native Kubernetes pods:
* **Monitors (`ceph-mon`):** Maintain maps of the cluster state and consensus. Essential for cluster health and coordination.
* **OSDs (Object Storage Daemons, `ceph-osd`):** Handle data storage, data replication, recovery, and rebalancing. Typically, each dedicated storage drive or disk partition maps to an OSD.
* **Managers (`ceph-mgr`):** Track runtime metrics, telemetry, and cluster performance data.
* **Metadata Servers (`ceph-mds`):** Required if using CephFS (shared file system) to store metadata for file hierarchies.
* **RADOS Gateway (`ceph-rgw`):** Provides an S3-compatible object storage interface.

---

## 4. Storage Provisioning Flow
1. **Persistent Volume Claim (PVC):** A user or application creates a standard Kubernetes PVC requesting storage from a configured Ceph `StorageClass`.
2. **Dynamic Provisioning:** The Rook-Ceph provisioner intercepts the request and dynamically allocates a block pool or file share within Ceph.
3. **Consumption:** Kubernetes provisions a Persistent Volume (PV) linked to the Ceph storage backend, allowing the application pod to safely read and write data across the distributed cluster.