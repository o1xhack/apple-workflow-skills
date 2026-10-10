import SwiftUI
import Foundation
struct Sample: View { var body: some View {
 AsyncImage(request: URLRequest(url: URL(string: "https://example.com/image.png")!))
  .asyncImageURLSession(URLSession.shared)
} }
