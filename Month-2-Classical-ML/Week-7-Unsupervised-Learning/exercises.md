# Week 7 exercises: Unsupervised learning

Theory reference: **`../../LEARNING_PATH.md`** (Month 2).

---

## A. K-Means

1. **Elbow**  
   Plot inertia (within-cluster sum of squares) vs k for k = 1 … 10. Mark your elbow choice.

2. **Silhouette**  
   Compute silhouette score for a few k values. Does it agree with the elbow?

3. **Initialization**  
   Run KMeans with different `random_state` for k=3. Are cluster labels stable?

4. **Scaling**  
   Cluster the same data with raw vs standardized features. Compare cluster assignments.

---

## B. Hierarchical clustering

5. **Linkage**  
   Compare `single`, `complete`, `average`, `ward` linkage on the same small dataset (dendrogram).

6. **Cut height**  
   Given a dendrogram, choose a cut that yields 3 vs 4 clusters; compare silhouette.

---

## C. PCA

7. **Variance explained**  
   Plot cumulative explained variance vs number of components. How many keep 90% / 95%?

8. **2D visualization**  
   Project Iris or Wine to 2D with PCA; color by true label (if available) — not cheating in real unsupervised, but helps learning.

9. **Reconstruction error**  
   Fit PCA with n components = 2 on scaled data; measure reconstruction MSE in original space.

---

## D. Other clustering & anomalies

10. **DBSCAN**  
    Cluster 2D blobs with noise with DBSCAN. Tune `eps` and `min_samples`; explain failure.

11. **t-SNE vs PCA**  
    Compare 2D PCA vs t-SNE visualization of the same standardized data (same random seed where possible).

12. **Isolation Forest**  
    Tune `contamination` or score threshold; identify top outliers and verify in feature space.

13. **Time series anomalies** (stretch)  
    Use rolling statistics + z-score or Isolation Forest on sequential features.

---

## E. Business case

14. **Customer segmentation**  
    Describe how you would explain 3 clusters to a non-technical stakeholder (profiles per cluster).

15. **GMM** (stretch)  
    Fit `GaussianMixture` with AIC/BIC for model selection on component count.

---

## Mini project: Customer segmentation

Cluster customers (e.g. **RFM**: recency, frequency, monetary) or transactional features.

**Deliverables:**
- Scaling and clustering method justified.
- Named segment descriptions + one business action per segment.
- Optional: simple dashboard or plots in notebook.
